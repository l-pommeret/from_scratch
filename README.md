Bonjour ! C'est juste un essai d'implémentation d'un réseau de neurones qui apprend *from scratch*. 

Dans `nn.py` vous pouvez faire fonctionner ces bribes de réseaux de neurones. évidemment, la descente de gradient implémentée est assez naïve (même pas stochastique), mais fonctionne pour des cas simples (convexes partout...).

`auto_derivation.py` implémente un algorithme qui dérive automatiquement n'importe quelle fonction dérivable composée des opérations `+`, `*`, `**`, `sin` et `cos`. Le gradient `gradient(f, *args)` étant simplement la liste des dérivées partielles de la fonction en un point donné. 

`gradient_descent.py` implémente la descente de gradient simple, avec pour seul hyperparamètre le `learning_rate`.

`nn.py` implémente un embryon de réseau de neurones qui permet un apprentissage. 