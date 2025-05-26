import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, roc_curve, confusion_matrix, auc, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
import numpy as np
import joblib, os

# Create folder for scalers and models
os.makedirs(os.path.join("..", "scaler"), exist_ok=True)
SCALER_PATHS = os.path.join("..", "scaler")


# ==========================
# 📊 Evaluate a Single Model
# ==========================
def evaluate_model(model, X, y, need_scaling=False, save_model=False, save_scaler=False):
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model_name = model.__class__.__name__

    print("\n" + "=" * 95)
    print(f"🧪 Evaluating Model: {model_name}")
    print("=" * 95)

    # ----------------------
    # 🔄 Apply Scaling
    # ----------------------
    if need_scaling:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        if save_scaler:
            scaler_filename = f'{SCALER_PATHS}/scaler_{model_name}.pkl'
            joblib.dump(scaler, filename=scaler_filename)
            print(f"💾 Scaler saved as: {scaler_filename}")

    # ----------------------
    # 🎯 Cross-validation
    # ----------------------
    cv_scores = cross_val_score(model, X_train, y_train, cv=skf, scoring='accuracy')
    mean_cv_acc = np.mean(cv_scores)

    # ----------------------
    # 🛠 Train & Predict
    # ----------------------
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"\n✅ Cross-Validation Accuracy: {mean_cv_acc:.4f}")
    print(f"🎯 Test Accuracy:            {acc:.4f}")
    print("\n🧾 Classification Report:")
    print(classification_report(y_test, y_pred))

    # ----------------------
    # 📉 Confusion Matrix
    # ----------------------
    cm = confusion_matrix(y_test, y_pred)
    plt.style.use("dark_background")
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['No Diabetes', 'Diabetes'],
                yticklabels=['No Diabetes', 'Diabetes'])
    plt.title(f"Confusion Matrix - {model_name}", fontsize=14)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show()

    # ----------------------
    # 💾 Save Model
    # ----------------------
    if save_model:
        model_filename = f'{SCALER_PATHS}/model_{model_name}.pkl'
        joblib.dump(model, filename=model_filename)
        print(f"💾 Model saved as: {model_filename}")

    # ----------------------
    # 📈 ROC Curve Values
    # ----------------------
    if hasattr(model, "predict_proba"):
        y_pred_prob = model.predict_proba(X_test)[:, 1]
    else:
        y_pred_prob = model.decision_function(X_test)
        y_pred_prob = (y_pred_prob - y_pred_prob.min()) / (y_pred_prob.max() - y_pred_prob.min())

    fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
    roc_auc = auc(fpr, tpr)

    return fpr, tpr, roc_auc, acc


# ==========================
# 📊 Comparison Plotting
# ==========================
def plot_model_comparisons(results):
    plt.style.use('dark_background')

    # ----------------------
    # 🔵 ROC Curves
    # ----------------------
    plt.figure(figsize=(10, 6))
    color_palette = ['cyan', 'magenta', 'orange', 'lime', 'red', 'deepskyblue', 'yellow']

    for i, (model_name, values) in enumerate(results.items()):
        fpr, tpr, auc_score, _ = values
        color = color_palette[i % len(color_palette)]
        plt.plot(fpr, tpr, label=f"{model_name} (AUC = {auc_score:.2f})", linewidth=2, color=color)

    plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label="Random Guess", linewidth=1.5)
    plt.title("🔥 ROC Curve Comparison - ENN Resampled", fontsize=14)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right", frameon=True)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ----------------------
    # 🎯 Accuracy Comparison
    # ----------------------
    plt.figure(figsize=(8, 5))
    model_names = list(results.keys())
    accuracies = [values[3] for values in results.values()]
    plt.barh(model_names, accuracies, color='limegreen')
    
    for i, acc in enumerate(accuracies):
        plt.text(acc + 0.005, i, f"{acc:.2f}", va='center', color='white')

    plt.title("🎯 Test Accuracy Comparison")
    plt.xlabel("Accuracy")
    plt.tight_layout()
    plt.show()
