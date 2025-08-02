
from sklearn.svm import SVC
from sklearn.metrics import zero_one_loss
from time import time
import numpy as np

results = []

X_train = np.random.rand(100, 10)
y_train = np.random.randint(0, 2, 100)
X_val = np.random.rand(20, 10)
y_val = np.random.randint(0, 2, 20)

# Exemple pour H3 = SVM polynôme degré 3
degree = 3
C_list = [0.1, 1, 10]
gamma_list = ['scale', 'auto']
coef0_list = [0, 1]

print("Démarrage de l'algorithme Complexity-Cost...")
print(f"Nombre de combinaisons à tester : {len(C_list) * len(gamma_list) * len(coef0_list)}")

for C in C_list:
    for gamma in gamma_list:
        for coef0 in coef0_list:
            
            # 1. Instancier le modèle
            model = SVC(kernel='poly', degree=degree, C=C, gamma=gamma, coef0=coef0)
            
            # 2. Mesurer le temps d'entraînement
            start = time()
            model.fit(X_train, y_train)
            train_time = time() - start
            
            # 3. Évaluer l'erreur de validation (f1)
            y_pred = model.predict(X_val)
            error_val = zero_one_loss(y_val, y_pred)
            
            # 4. Estimer la complexité (f2) — ici d^p
            d = X_train.shape[1]
            complexity = d ** degree
            
            # 5. Estimer le coût (f3) — ici temps d'entraînement
            cost = train_time
            
            # 6. Sauvegarder le triplet
            results.append({
                'model': model,
                'params': {'C': C, 'gamma': gamma, 'coef0': coef0},
                'f1_error': error_val,
                'f2_complexity': complexity,
                'f3_cost': cost
            })
            
            print(f"C={C}, gamma={gamma}, coef0={coef0} -> Error: {error_val:.4f}, Cost: {cost:.4f}s")

print(f"\nAlgorithme terminé ! {len(results)} modèles testés.")
print("\nMeilleur modèle (erreur la plus faible):")
best_model = min(results, key=lambda x: x['f1_error'])
print(f"Paramètres: {best_model['params']}")
print(f"Erreur: {best_model['f1_error']:.4f}")
print(f"Coût: {best_model['f3_cost']:.4f}s")
