- #### Utilisation du polymorphisme (lien dans votre code) + définition
[Classe Capitalize ](models/Word/Capitalize.py) 

Le polymorphisme est un concept qui permet à des objets de différentes classes de répondre de manière différente à une même méthode ou fonction. Cela signifie que des objets de classes différentes peuvent être traités de manière uniforme en utilisant une interface commune. Le polymorphisme facilite la réutilisation du code, car les mêmes opérations peuvent être appliquées à des objets de types différents, sans avoir besoin de connaître leur type spécifique. Cela favorise une plus grande flexibilité et extensibilité du code, ainsi qu'une meilleure abstraction des détails d'implémentation spécifiques aux classes individuelles.

- #### Utilisation de l'encapsulation (lien dans votre code) + définition

[Classe ManageWords](models/Word/ManageWords.py)

L'encapsulation consiste à regrouper des données et les méthodes qui les manipulent dans une même entité appelée classe. L'encapsulation permet de cacher les détails internes et la complexité d'une classe en exposant uniquement une interface publique claire et cohérente. Cela permet de contrôler l'accès aux données et de les protéger contre des modifications non autorisées. L'encapsulation favorise également la modularité et la réutilisabilité du code, car les modifications internes d'une classe n'affectent pas les autres parties du programme qui l'utilisent, à condition que l'interface publique reste inchangée.

- #### Utilisation de composition (lien dans votre code) + définition
[Classe Engine : Composition dans les fonctions update words](models/Engine.py) : 
````python
    def _process_options(self):
        if 'date' in self.options:
            self._update_words(Date(self.get_words()).possibilities)
        if 'upper' in self.options:
            self._update_words(Uppercase(self.get_words()).possibilities)
        if 'lower' in self.options:
            self._update_words(Lowercase(self.get_words()).possibilities)
        if 'capitalize' in self.options:
            self._update_words(ToCapitalize(self.get_words()).possibilities)
        if 'leet' in self.options:
            self._update_words(Leet(self.get_words()).possibilities)
        if 'accent' in self.options:
            self._update_words(Accent(self.get_words()).possibilities)
        if 'char' in self.options:
            self._update_words(SpecialChar().get_special_characters())
        return self.get_words()

    def _update_words(self, new_words):
        self._words = list(set(self._words + new_words))
````

La composition est utilisée afin de créer des relations entre des objets en les combinant pour former une structure plus complexe. Celle ci est basée sur le principe de "tout est un objet" et consiste à inclure un objet en tant que membre d'un autre objet. Cela signifie qu'un objet est composé d'autres objets et peut les utiliser pour étendre ses fonctionnalités ou déléguer certaines tâches. Elle permet de construire des relations de dépendance entre les objets de manière flexible, en favorisant la réutilisabilité du code et en permettant de créer des structures complexes à partir de composants simples et autonomes.

- #### Utilisation de l'héritage (lien dans votre code) + définition
[Classe Lowercase : Heritage de ManageWords ](models/Word/Lowercase.py) : 

L'héritage permet d'étendre et de spécialiser les fonctionnalités d'une classe existante, de créer une hiérarchie de classes et de favoriser la réutilisabilité du code.

- #### Utilisation d'interface (lien dans votre code) + définition

[Classe ManageWords](models/Word/ManageWords.py)

L'interface définit un contrat comportemental que les classes doivent respecter en implémentant les méthodes spécifiées. Elle permet d'abstraire les détails d'implémentation et facilite l'interaction entre les classes, favorisant ainsi la flexibilité et la modularité du code.

- #### Utilisation de méthodes et attributs d'objets (lien dans votre code) + définition

[Classe Engine => Ligne 17 ](models/Engine.py)

Les méthodes et les attributs permettent de définir le comportement et l'état des objets. Les méthodes représentent les actions que les objets peuvent effectuer, tandis que les attributs représentent les données qu'ils contiennent. Ils sont utilisés pour encapsuler la logique et les données d'un objet, facilitant ainsi la modularité, la réutilisabilité et la gestion des objets dans un programme.

- #### Utilisation de méthodes et attributs statiques (lien dans votre code) + définition

[Classe Date ](models/Word/Date.py)

Les méthodes et attributs statiques permettent d'accéder à des fonctionnalités ou des données spécifiques à une classe sans avoir besoin de créer des instances de cette classe. Ils offrent une utilisation pratique pour des fonctionnalités qui ne nécessitent pas de manipuler l'état de l'objet ou qui sont indépendantes des instances individuelles.

- #### Utilisation de méthodes et attributs de classe (lien dans votre code) + définition

[Classe SpecialChar](models/Word/SpecialChar.py)

Les méthodes et attributs de classe offrent une fonctionnalité liée à la classe dans son ensemble, qui peut être partagée par toutes les instances de cette classe. Ils permettent d'accéder et de manipuler des données ou des fonctionnalités spécifiques à la classe sans avoir besoin de créer des instances de cette classe.