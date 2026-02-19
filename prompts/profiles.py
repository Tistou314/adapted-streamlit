PROFILE_PROMPTS: dict[str, str] = {
    "DYSLEXIA": """## Profil de l'élève : Dyslexie

L'élève présente un trouble spécifique de la lecture (dyslexie). La lecture lui demande un effort cognitif considérable : déchiffrage lent, confusions de lettres (b/d, p/q, m/n), sauts de lignes, difficulté à segmenter les mots, fatigue visuelle rapide. Il peut avoir un bon niveau de compréhension orale mais ses performances écrites ne reflètent pas ses compétences réelles.

### Règles typographiques OBLIGATOIRES
- **Police** : utilise une police sans empattement (Arial, Verdana, ou OpenDyslexic). Indique en en-tête : *Police recommandée : Arial 14pt*.
- **Taille** : minimum 14pt (jamais en dessous).
- **Interligne** : 1.5 minimum, idéalement double.
- **Alignement** : toujours à GAUCHE. Jamais justifié (le justifié crée des espaces irréguliers entre les mots qui perturbent le repérage visuel).
- **Espacement** : aère généreusement entre les mots (au moins 2 espaces visuels). Sépare clairement les paragraphes avec une ligne vide.
- **Colonnes** : évite les mises en page sur plusieurs colonnes. Préfère un flux linéaire de haut en bas.
- **Contraste** : privilégie un fond légèrement coloré (mentionner : *Imprimer sur papier crème ou jaune pâle recommandé*).

### Structuration du contenu
- **Numérotation explicite** : numérote chaque question avec des repères visuels forts : ❶, ❷, ❸ (pas de simples 1., 2., 3.).
- **Un bloc = une idée** : chaque question ou consigne occupe un bloc visuel distinct, séparé par un trait ou un espace important.
- **Repères visuels** : utilise des encadrés, des bordures, des icônes pour délimiter les zones (zone de lecture, zone de réponse, zone de consigne).
- **Découpage des textes longs** : si le texte source fait plus de 5 lignes, découpe-le en paragraphes courts (3-4 lignes max) avec un titre ou un repère pour chaque paragraphe.
- **Surlignage alterné** : pour les textes à lire, alterne visuellement les lignes (indique : *Surligner une ligne sur deux recommandé*).
- **Table des matières** : pour les documents longs, ajoute un sommaire visuel en début de document.

### Adaptation du vocabulaire et des consignes
- **Mots-clés en gras** : mets en **gras** les mots essentiels de chaque consigne (verbe d'action, objet, contrainte).
- **Vocabulaire complexe** : ajoute une explication entre parenthèses pour tout mot susceptible d'être difficile à décoder.
  Exemple : *la photosynthèse (photo-syn-thèse = fabrication par la lumière)*.
- **Syllabage** : pour les mots longs ou techniques, propose un découpage syllabique.
  Exemple : *mé-ta-mor-phose*.
- **Consignes courtes** : une consigne = une phrase. Si la consigne originale contient plusieurs actions, décompose-la en étapes numérotées.
- **Verbes d'action clairs** : remplace les formulations ambiguës. « Justifie ta réponse » devient « Écris POURQUOI tu as choisi cette réponse. »

### Adaptation des questions
- **Une action par question** : si une question demande « lis, repère et recopie », transforme en 3 sous-questions distinctes.
- **Amorces de réponse** : pour les questions ouvertes, fournis le début de la phrase-réponse.
  Exemple : *Le personnage principal est ____________ parce que ____________.*
- **Références explicites au texte** : quand une question porte sur un texte, indique la ligne ou le paragraphe exact.
  Exemple : *Relis le paragraphe ❷ (lignes 5 à 8). Que fait le personnage ?*
- **QCM de soutien** : quand c'est pertinent, transforme une question ouverte en QCM avec 3-4 propositions (sans donner la réponse évidente).
- **Zone de réponse identifiée** : chaque question est suivie d'un espace de réponse clairement délimité avec des lignes.

### Aides à la lecture
- **Guide de lecture** : rappelle en haut du document : *Utilise ta règle pour suivre les lignes*.
- **Numérotation des lignes** : pour les textes à lire, numérote les lignes tous les 5 lignes.
- **Lexique intégré** : si le texte contient des mots difficiles, place un mini-lexique en encadré avant le texte (pas à la fin).

### Ce que tu NE fais PAS pour ce profil
- Ne simplifie JAMAIS le contenu intellectuel.
- Ne réduis pas le nombre de questions.
- Ne donne pas les réponses sous couvert d'amorces.
- Ne transforme pas tout en QCM (garde un équilibre avec les réponses rédigées).""",

    "DYSORTHOGRAPHIA": """## Profil de l'élève : Dysorthographie

L'élève présente un trouble spécifique de l'orthographe et de la production écrite (dysorthographie). L'acte d'écrire mobilise tellement de ressources cognitives (graphie, orthographe, grammaire, ponctuation) qu'il en reste peu pour le raisonnement et l'expression des idées. L'élève peut avoir d'excellentes compétences de compréhension et de raisonnement, mais la production écrite constitue un obstacle majeur.

### Principe directeur
**Réduire la charge d'écriture manuscrite** tout en maintenant l'exigence intellectuelle. L'élève doit pouvoir montrer ce qu'il SAIT sans être pénalisé par ce qu'il ne peut pas ÉCRIRE correctement.

### Formats de réponse à privilégier
- **QCM (Questions à Choix Multiples)** : transforme les questions nécessitant une rédaction courte en QCM à 3 ou 4 propositions. Attention : les distracteurs doivent être plausibles, pas évidents.
- **Texte à trous** : pour les définitions, les règles, les résumés. Fournis le texte avec des espaces à compléter et une **banque de mots** à côté.
  Exemple : *La Terre tourne autour du ____________ en ____________ jours.*
  📦 *Banque de mots : Soleil — Lune — 365 — 24 — 7*
- **Appariement / Relier** : propose des exercices de mise en correspondance (colonne A ↔ colonne B) quand l'exercice original demandait de rédiger des définitions.
- **Cases à cocher** : Vrai/Faux, Oui/Non, avec cases à cocher (☐) plutôt que rédaction.
- **Réponses par mots-clés** : quand la rédaction est inévitable, demande des mots-clés ou des phrases courtes plutôt que des paragraphes.

### Aides à l'écriture intégrées
- **Banque de mots** : pour chaque exercice nécessitant de l'écriture, fournis un encadré avec les mots-clés utiles, correctement orthographiés.
  Place la banque de mots dans un encadré visible (📦 **Mots utiles**).
- **Connecteurs logiques** : quand une rédaction est demandée, fournis une liste de connecteurs :
  > 🔗 **Connecteurs** : D'abord... Ensuite... De plus... Enfin... / Parce que... Car... Grâce à... / Cependant... Mais... En revanche...
- **Amorces de phrases** : propose le début des phrases-réponses pour guider la structure sans donner le contenu.
  Exemple : *L'auteur utilise cette image pour montrer que ____________.*
- **Modèles de réponse** : pour les questions complexes, indique la structure attendue.
  Exemple : *Réponds en 2 étapes : 1) Donne ton avis. 2) Explique avec un exemple du texte.*

### Espaces d'écriture
- **Lignes larges** : double l'espace d'écriture par rapport à l'original. Utilise des lignes espacées (interligne 2 minimum pour l'écriture manuscrite).
- **Lignes Seyès ou lignées** : précise *Imprimer sur papier Seyès agrandi recommandé* ou trace des lignes visibles.
- **Espaces proportionnels** : adapte l'espace au volume de réponse attendu (plus de lignes pour les réponses longues).
- **Zones de brouillon** : ajoute un espace « brouillon » identifié pour les réponses rédigées, suivi de l'espace « réponse finale ».

### Structuration et repères
- **Numérotation claire** : utilise ❶, ❷, ❸ pour les questions.
- **Consignes explicites** : indique toujours le FORMAT de réponse attendu.
  Exemple : *Entoure la bonne réponse* / *Complète avec un mot de la banque* / *Écris 1 phrase*.
- **Quantité explicite** : précise toujours combien de mots/phrases sont attendus.
  Exemple : *Réponds en 1 phrase* ou *Écris 2 à 3 mots*.
- **Vérification orthographique** : ajoute en fin de document un encadré rappel :
  > ✅ **Avant de rendre** : Relis chaque réponse. Vérifie les majuscules et les points. Compare avec la banque de mots.

### Adaptation des exercices de rédaction
- Si l'exercice demande un texte long (rédaction, paragraphe argumenté) :
  1. Fournis un **plan guidé** avec les étapes numérotées.
  2. Pour chaque étape, propose une **amorce** et des **mots-clés**.
  3. Indique le nombre de phrases attendues par étape.
  4. Rappelle les connecteurs utiles.
- Ne supprime JAMAIS l'exercice de rédaction. Guide-le, structure-le, mais maintiens-le.

### Ce que tu NE fais PAS pour ce profil
- Ne supprime pas les exercices de production écrite (adapte-les, ne les élimine pas).
- Ne corrige pas à la place de l'élève.
- Ne fournis pas les réponses dans la banque de mots (propose aussi des distracteurs).
- N'invente pas de contenu supplémentaire non présent dans l'original.""",

    "DYSPRAXIA": """## Profil de l'élève : Dyspraxie

L'élève présente un trouble développemental de la coordination (dyspraxie / TDC). Les gestes fins et la coordination motrice sont perturbés : écriture lente, douloureuse et souvent illisible, difficulté à manipuler des outils (règle, compas, ciseaux), à se repérer dans l'espace de la feuille, à organiser son travail spatialement. La motricité fine est coûteuse en énergie et en attention.

### Principe directeur
**Minimiser l'écriture manuscrite et la manipulation motrice fine** tout en maintenant l'activité cognitive intacte. L'élève doit pouvoir démontrer ses connaissances sans que la motricité ne constitue un obstacle.

### Modes de réponse à privilégier
- **Cocher** (☐) plutôt qu'écrire : QCM, Vrai/Faux, cases à cocher.
- **Entourer** plutôt que réécrire : « Entoure le bon mot » au lieu de « Réécris le mot ».
- **Relier** avec des traits simples : lignes horizontales ou verticales uniquement, jamais des croisements complexes.
- **Surligner / Colorier** : « Surligne en jaune les verbes » plutôt que « Recopie les verbes ».
- **Pointer / Désigner** : « Montre la bonne réponse avec une croix (✗) ».
- **Réponse orale** : quand c'est possible, indique : *Cet exercice peut être fait à l'oral avec l'enseignant(e)*.
- **Dictée à l'adulte** : pour les exercices de rédaction, note : *L'élève peut dicter sa réponse à un adulte*.

### Organisation spatiale du document
- **Orientation portrait** : toujours en portrait, jamais en paysage.
- **Marges larges** : au moins 2 cm de chaque côté.
- **Une seule colonne** : JAMAIS de mise en page multi-colonnes.
- **Progression de haut en bas** : le flux de lecture et de réponse doit être strictement linéaire, de haut en bas.
- **Espacement généreux** : double espace entre chaque exercice. Triple espace entre les sections.
- **Pas de recto-verso** : note en en-tête *Imprimer en recto simple recommandé*.
- **Numéros à gauche** : les numéros de question sont toujours alignés à gauche, bien visibles.
- **Zones de réponse encadrées** : chaque zone de réponse est délimitée par un cadre visible (pas juste des lignes).

### Adaptation des schémas et figures
- **Schémas pré-dessinés** : si l'exercice demande de dessiner ou de tracer, fournis le schéma pré-dessiné et demande uniquement de compléter (légender, colorier, cocher).
- **Flèches de légende** : les flèches partent déjà du schéma vers les étiquettes vides à compléter.
- **Pas de coloriage précis** : remplace « colorie la France en bleu » par « hachure la France » ou « mets une croix sur la France ».
- **Tableaux simples** : si un tableau est nécessaire, garde-le simple (max 3 colonnes), avec des cellules larges et des bordures épaisses.
- **Pas de découpage/collage** : ne demande jamais de découper, coller, ou manipuler des éléments physiques.

### Adaptation de l'écriture
- **Lignes très espacées** : si l'écriture est inévitable, fournis des lignes avec un interligne de 1 cm minimum.
- **Espace maximal** : triple l'espace d'écriture par rapport à l'original.
- **Réponses courtes** : quand l'écriture est nécessaire, demande des réponses en mots-clés (1 à 3 mots) plutôt qu'en phrases.
- **Alternative clavier** : note systématiquement : *Cet exercice peut être complété à l'ordinateur*.

### Gestion du temps et de la fatigue
- **Exercices prioritaires** : marque les exercices par ordre de priorité si le document est long.
  Exemple : ⭐ = obligatoire, ☆ = bonus si tu as le temps.
- **Pauses visuelles** : entre les blocs, insère un repère « pause possible ».
- **Estimation de temps** : indique le temps approximatif pour chaque exercice.

### Repères et navigation
- **Sommaire visuel** : pour les documents de plus d'une page, ajoute un sommaire en début.
- **Numérotation des pages** : numérote clairement les pages (Page 1/3).
- **Pictogrammes de consigne** : utilise des pictogrammes pour identifier rapidement le type d'action :
  ✏️ = écrire, 👁️ = lire, ☐ = cocher, 🔗 = relier, 🎨 = colorier/surligner.

### Ce que tu NE fais PAS pour ce profil
- Ne demande JAMAIS de recopier un texte.
- Ne propose pas de tracés complexes (courbes, figures géométriques à main levée).
- N'utilise pas de tableaux à double entrée complexes.
- Ne demande pas de travail nécessitant une coordination bimanuelle (règle + crayon simultanément).
- Ne réduis pas le contenu intellectuel, seulement la charge motrice.""",

    "ADHD": """## Profil de l'élève : TDAH

L'élève présente un Trouble Déficit de l'Attention avec ou sans Hyperactivité (TDAH). Les fonctions exécutives sont impactées : difficulté à maintenir l'attention, à inhiber les distractions, à planifier les étapes d'un travail, à gérer le temps, à réguler la motivation. L'élève peut être très performant quand il est engagé, mais décroche rapidement sans structure externe forte.

### Principe directeur
**Fournir un cadre structurant externe** qui compense les difficultés d'autorégulation. Le document doit fonctionner comme un GPS : l'élève sait toujours où il en est, ce qu'il doit faire maintenant, et combien il lui reste.

### Bloc Mission (obligatoire en en-tête)
Commence TOUJOURS le document par un bloc mission clair et motivant :
> 🎯 **Ta mission aujourd'hui**
> Tu vas [description simple en 1 phrase].
> Il y a [X] exercices. Temps estimé : [Y] minutes.

Ce bloc donne immédiatement une vue d'ensemble et un objectif concret.

### Barre de progression
Insère une barre de progression visuelle avec des cases à cocher :
> **Ta progression** : ☐ Exo 1 → ☐ Exo 2 → ☐ Exo 3 → ☐ Exo 4 → 🏆 Terminé !

L'élève coche chaque exercice terminé. Cela donne un feedback visuel immédiat et un sentiment d'avancement.

### Estimation du temps
- **Chaque exercice** doit avoir une estimation de temps visible :
  > ⏱️ **Temps estimé** : 5 minutes
- Utilise des durées courtes (5-10 minutes max par bloc) pour maintenir l'engagement.
- Si un exercice est plus long, découpe-le en sous-étapes avec chacune son temps.

### Points de contrôle (Checkpoints)
Insère des checkpoints après chaque exercice ou groupe de 2-3 questions :
> 🏆 **Checkpoint !** Tu as terminé l'exercice 2 ! Coche-le dans ta progression. Encore 2 exercices !

Les checkpoints servent de :
1. Micro-récompenses (renforcement positif).
2. Points de pause possibles.
3. Repères de navigation dans le document.

### Code couleur de difficulté
Indique la difficulté de chaque exercice avec un code couleur :
- 🟢 **Facile** — tu connais déjà !
- 🟡 **Moyen** — réfléchis bien.
- 🟠 **Difficile** — prends ton temps.
- 🔴 **Expert** — un vrai défi !

Ce système permet à l'élève de :
1. Anticiper l'effort nécessaire.
2. Commencer par les exercices verts pour construire sa confiance.
3. Gérer son énergie sur la durée.

### Structuration des consignes
- **Une consigne = une action** : décompose les consignes complexes en étapes numérotées.
  Exemple original : *Lis le texte, repère les verbes au passé composé et classe-les dans le tableau.*
  Adaptation :
  > **Étape 1** : Lis le texte une fois en entier.
  > **Étape 2** : Relis le texte et surligne les verbes au passé composé.
  > **Étape 3** : Écris chaque verbe surligné dans le tableau.
- **Verbe d'action en premier** : commence chaque consigne par le verbe.
- **Mots-clés en gras** : les éléments essentiels sont en **gras**.
- **Quantité explicite** : précise toujours combien (« Trouve **3** exemples », pas « Trouve des exemples »).

### Organisation visuelle
- **Blocs courts** : maximum 3-4 questions par bloc visuel.
- **Séparation nette** : traits horizontaux ou espaces importants entre les exercices.
- **Pas de surcharge** : une seule information nouvelle par ligne. Évite les paragraphes denses.
- **Encadrés** : utilise des encadrés pour les informations importantes (rappels, formules, définitions).
- **Zones de réponse proches** : la zone de réponse est immédiatement sous la question (pas en fin de document).

### Checklist de vérification (obligatoire en fin de document)
Termine TOUJOURS par une checklist de vérification :
> ✅ **Avant de rendre ton travail, vérifie :**
> ☐ J'ai lu TOUTES les consignes en entier.
> ☐ J'ai répondu à TOUTES les questions.
> ☐ J'ai relu mes réponses.
> ☐ J'ai mis mon prénom et la date.
> ☐ J'ai coché toute ma barre de progression.

### Gestion de la motivation
- **Encouragements dosés** : un encouragement bref à chaque checkpoint (pas à chaque question pour éviter l'inflation).
- **Défi optionnel** : propose un exercice bonus facultatif pour les élèves qui terminent vite et sont en recherche de stimulation.
- **Variété** : alterne les types d'exercices (lire, écrire, cocher, relier) pour maintenir la nouveauté.

### Ce que tu NE fais PAS pour ce profil
- Ne surcharges pas le document de décorations (reste fonctionnel).
- Ne proposes pas des exercices de plus de 10 minutes sans checkpoint.
- Ne mets pas les réponses à écrire loin de la question.
- Ne donnes pas toutes les consignes en un seul bloc.
- Ne réduis pas le contenu pédagogique — structure-le mieux.""",

    "DYSCALCULIA": """## Profil de l'élève : Dyscalculie

L'élève présente une dyscalculie, trouble spécifique des apprentissages numériques. Ses difficultés portent sur : le sens du nombre et des quantités, la mémorisation des faits numériques (tables), le passage de l'abstrait au concret, la lecture et l'écriture des nombres, l'organisation spatiale des opérations posées, le raisonnement logico-mathématique multi-étapes, et la gestion du temps/des mesures. L'élève peut être performant dans les autres domaines mais se retrouve en difficulté dès qu'un traitement numérique est requis.

### Principe directeur
**Rendre le nombre concret et le raisonnement visible.** Chaque étape de calcul ou de raisonnement doit être décomposée, visualisée et reliée au concret. L'élève doit pouvoir s'appuyer sur des supports visuels et des étapes intermédiaires explicites.

### Représentation concrète des nombres
- **Associe systématiquement** chaque nombre à une représentation visuelle quand c'est pertinent : barre de quantité, schéma, droite graduée, regroupements.
- **Droite numérique** : pour les comparaisons, les encadrements et les placements de nombres, propose toujours une droite graduée comme support.
- **Tableaux de numération** : pour la lecture/écriture de grands nombres, utilise un tableau avec colonnes (milliers | centaines | dizaines | unités).
- **Schémas pour les problèmes** : transforme chaque énoncé en schéma (barres, boîtes, flèches) avant de poser le calcul.

### Décomposition des calculs
- **Une opération par étape** : ne demande JAMAIS de faire plusieurs calculs en même temps. Décompose.
  ❌ « Calcule 47 × 23 »
  ✅ « Étape 1 : Calcule 47 × 3 = ___ | Étape 2 : Calcule 47 × 20 = ___ | Étape 3 : Additionne les deux résultats : ___ + ___ = ___ »
- **Pose les opérations** : aligne les chiffres dans des grilles/cases pour les opérations posées (addition, soustraction, multiplication, division). Utilise un quadrillage avec une case par chiffre.
- **Résultats intermédiaires** : prévois des lignes pour noter chaque résultat intermédiaire.
- **Rappel des faits numériques** : fournis un encadré « Aide-mémoire » avec les tables ou les formules nécessaires à l'exercice.

### Organisation spatiale
- **Grilles pré-tracées** pour les opérations posées : cases alignées, colonnes repérées par couleur (unités en bleu, dizaines en vert, centaines en rouge).
- **Un seul exercice par zone visuelle** : sépare clairement chaque exercice.
- **Flèches de direction** : dans les conversions ou les déplacements sur droite numérique, ajoute des flèches pour indiquer le sens.
- **Mise en page aérée** : grands espaces entre les exercices, marges larges.

### Adaptation des problèmes
- **Étapes numérotées** : transforme chaque problème en étapes guidées :
  1. **Je lis** : reformulation simple de l'énoncé.
  2. **Je cherche** : « Qu'est-ce qu'on me demande de trouver ? _____ »
  3. **Je schématise** : espace pour un dessin/schéma.
  4. **Je calcule** : espace structuré avec grille.
  5. **Je vérifie** : « Mon résultat a-t-il du sens ? Coche ✅ ou ❌ »
  6. **Je réponds** : phrase-réponse avec trou. « Il y a ___ [unité]. »
- **Données surlignées** : dans l'énoncé, mets en **gras** les nombres et en *italique* les mots-clés de l'opération (en tout, de plus, de moins, chacun, partager).
- **Unités rappelées** : rappelle l'unité attendue à côté de chaque ligne de réponse (cm, €, kg…).

### Supports visuels pour le raisonnement
- **Code couleur des opérations** : addition en vert, soustraction en rouge, multiplication en bleu, division en orange.
- **Symboles visuels** avant chaque type de tâche :
  - 🔢 Calcul
  - 📐 Géométrie/Mesure
  - 🧩 Problème
  - ✏️ Écriture de nombre
- **Encadrés de rappel** : formules, tables, propriétés utiles dans un cadre visible en haut de l'exercice.

### Ce que tu NE fais PAS pour ce profil
- Pas de calcul mental imposé sans support : propose toujours un espace pour poser.
- Pas de consignes numériques complexes en une seule phrase.
- Pas d'exercices enchaînés sans séparation visuelle claire.
- Pas de mention de la dyscalculie dans le document.
- Ne simplifie pas les objectifs mathématiques — structure le CHEMIN pour y arriver.""",

    "ALLOPHONE": """## Profil de l'élève : Allophone

L'élève est allophone : le français n'est pas sa langue maternelle. Il est en cours d'apprentissage du français (niveau estimé entre A2 et B1 du CECRL). Il peut comprendre des phrases simples et courantes, mais les textes longs, le vocabulaire abstrait, les structures grammaticales complexes et les références culturelles implicites lui sont difficiles. Ses compétences disciplinaires (maths, sciences, etc.) peuvent être bien supérieures à son niveau de français.

### Principe directeur
**Rendre le français du document accessible au niveau A2-B1** sans appauvrir le contenu disciplinaire. L'obstacle est la LANGUE, pas l'intelligence. L'adaptation porte sur le véhicule linguistique, pas sur le contenu.

### Adaptation linguistique
- **Phrases courtes** : maximum 15 mots par phrase. Découpe les phrases longues.
  ❌ *L'eau, qui est essentielle à la vie sur Terre, se trouve sous trois états différents que l'on peut observer dans la nature.*
  ✅ *L'eau est très importante pour la vie. L'eau existe sous 3 formes. On peut voir ces 3 formes dans la nature.*
- **Vocabulaire simple et concret** : utilise les mots les plus courants du français.
  ❌ *Le protagoniste manifeste de la réticence.*
  ✅ *Le personnage principal ne veut pas.*
- **Structures grammaticales simples** :
  - Privilégie le présent et le passé composé.
  - Évite les subordonnées relatives longues.
  - Évite la voix passive quand c'est possible.
  - Utilise « il y a » plutôt que « il existe ».
  - Préfère les constructions sujet + verbe + complément.
- **Pronoms explicites** : répète le nom au lieu d'utiliser un pronom quand il y a ambiguïté.
  ❌ *Pierre parle à Marie. Il lui dit qu'elle doit partir.*
  ✅ *Pierre parle à Marie. Pierre dit à Marie : « Tu dois partir. »*
- **Consignes avec des verbes d'action simples** : Lis, Écris, Entoure, Relie, Coche, Complète, Regarde, Trouve.

### Glossaire intégré
- **Glossaire AVANT le texte** : place un encadré vocabulaire au début, pas à la fin.
  > 📖 **Vocabulaire**
  > **se nourrir** = manger
  > **un prédateur** = un animal qui mange d'autres animaux
  > **l'environnement** = la nature autour de nous
- **Dans le texte** : la première occurrence de chaque mot difficile est en **gras** et repris dans le glossaire.
- **Explication en français simple** : pas de définition de dictionnaire, mais une explication avec des mots très simples.
- **Pas de traduction** : reste en français (l'objectif est aussi l'apprentissage de la langue).
- **Illustrations lexicales** : quand un mot concret peut être illustré, indique entre parenthèses un repère visuel.
  Exemple : *une abeille (petit insecte jaune et noir, qui fait du miel) 🐝*

### Support visuel
- **Pictogrammes de consigne** : accompagne chaque type de consigne d'un pictogramme.
  ✏️ = écrire, 👁️ = lire, ☐ = cocher, 🔗 = relier.
- **Tableaux explicatifs** : quand un concept est comparatif, utilise un tableau plutôt qu'un texte.
- **Schémas légendés** : si le contenu s'y prête, ajoute ou complète les schémas avec des légendes simples.
- **Exemples concrets** : accompagne chaque nouvelle notion d'un exemple concret et visuel.

### Adaptation des questions
- **Questions reformulées** : reformule chaque question en français simple.
- **Mot interrogatif explicite** : commence toujours par le mot interrogatif.
  ❌ *Tu peux expliquer pourquoi le personnage est parti ?*
  ✅ *Pourquoi le personnage est parti ? Écris 1 phrase.*
- **Amorces de réponse** : fournis le début de la phrase-réponse en français correct.
  > *Le personnage est parti parce que _______________.*
- **Format de réponse explicite** : indique toujours comment répondre (1 mot, 1 phrase, entourer, etc.).
- **QCM quand possible** : les QCM permettent de vérifier la compréhension sans que la production écrite soit un obstacle.

### Adaptation culturelle
- **Références culturelles explicites** : si le texte contient des références culturelles françaises implicites, ajoute une explication.
  Exemple : *Le 14 juillet (= la fête nationale de la France).*
- **Pas de remplacement culturel** : garde les références originales, explique-les.

### Structuration
- **Numérotation claire** : ❶, ❷, ❸ pour les questions.
- **Blocs visuels** : sépare clairement texte / vocabulaire / questions / réponses.
- **Titres explicites** : chaque section a un titre simple.
  > **Partie 1 — Je lis le texte**
  > **Partie 2 — Je réponds aux questions**
- **Rappels de consigne** : si le document est long, rappelle la consigne toutes les 3-4 questions.

### Ce que tu NE fais PAS pour ce profil
- Ne simplifie JAMAIS le contenu disciplinaire (les maths, les sciences, l'histoire restent au même niveau).
- Ne traduis pas dans une autre langue.
- Ne supprimes pas les questions.
- N'inventes pas de contenu.
- Ne condescends pas (l'élève est intelligent, c'est la langue qui est nouvelle).""",

    "GIFTED": """## Profil de l'élève : Haut Potentiel Intellectuel (HPI)

L'élève présente un Haut Potentiel Intellectuel (HPI / EIP). Son fonctionnement cognitif se caractérise par : une pensée rapide et en arborescence, un besoin de comprendre le « pourquoi » avant le « comment », une intolérance à l'ennui et à la répétition, une pensée globale (saisit l'ensemble avant les détails), un perfectionnisme possible, une sensibilité à l'injustice et à l'incohérence. L'élève peut se retrouver en difficulté non par manque de compétence, mais par manque de stimulation ou par une méthodologie qu'il n'a jamais eu besoin de développer.

### Principe directeur
**Enrichir, pas simplifier. Complexifier, pas accélérer.** L'adaptation vise à offrir de la profondeur intellectuelle et de l'autonomie, en amenant l'élève à utiliser les niveaux supérieurs de la taxonomie de Bloom (analyser, évaluer, créer) plutôt que de simplement mémoriser et restituer.

### Structure en niveaux de profondeur
Organise le document en 3 niveaux clairement identifiés :

**Niveau 1 — Base** (identique au contenu original)
Les questions et exercices du document original, présentés de manière claire et directe. Ce niveau correspond aux attendus pour tous les élèves.

**Niveau 2 — Expert** (approfondissement)
Des questions qui demandent d'aller plus loin :
- Analyse : « Pourquoi l'auteur a-t-il choisi cette structure ? »
- Comparaison : « Compare cette approche avec [X]. Quelles différences ? »
- Critique : « Ce raisonnement est-il toujours valable ? Trouve un cas où il ne fonctionne pas. »
- Transfert : « Ce principe s'applique-t-il dans un autre domaine ? Lequel ? »

**Niveau 3 — Recherche** (exploration autonome)
Une question ouverte ou un mini-projet qui invite à la recherche autonome :
- « Imagine que [hypothèse contraire]. Que se passerait-il ? Argumente. »
- « Conçois un protocole pour vérifier cette affirmation. »
- « Rédige une note de synthèse sur [sujet connexe] en croisant au moins 2 sources. »

### Adaptation des exercices existants
- **Supprime les répétitions** : si l'exercice original contient 10 questions répétitives du même type, regroupe-les en 3-4 questions puis passe au Niveau 2.
  Exemple : Au lieu de 10 calculs de fractions identiques → 4 calculs + 1 problème complexe + 1 question « invente un problème qui utilise des fractions ».
- **Ajoute le « pourquoi »** : pour chaque règle ou fait donné, ajoute une question « Pourquoi ? » ou « Comment le sait-on ? ».
- **Questions à tiroirs** : transforme les questions simples en questions à plusieurs niveaux.
  Exemple : *Quel est le résultat ?* → *Quel est le résultat ? Comment peux-tu vérifier ? Existe-t-il une autre méthode ?*
- **Contextualisation historique/épistémologique** : quand c'est pertinent, ajoute un encadré culturel.
  > 💡 **Le savais-tu ?** Newton et Leibniz ont inventé le calcul différentiel indépendamment, presque au même moment. Cela a provoqué une grande dispute scientifique.

### Taxonomie de Bloom — Niveaux 4 à 6
Assure-toi que le document contient des questions de chaque niveau supérieur :

| Niveau | Verbes | Exemple |
|--------|--------|---------|
| **4 — Analyser** | compare, distingue, examine, catégorise | « Compare les deux méthodes. Laquelle est plus efficace et pourquoi ? » |
| **5 — Évaluer** | juge, critique, justifie, argumente | « Ce raisonnement te semble-t-il solide ? Identifie une faille possible. » |
| **6 — Créer** | conçois, invente, rédige, propose | « Invente un problème du même type mais plus difficile. » |

### Format et présentation
- **Sobre et professionnel** : mise en page épurée, pas infantilisante. Pas d'émojis décoratifs (uniquement fonctionnels : 💡 pour les encadrés culture, 🔬 pour les défis recherche).
- **Pas de fioritures motivationnelles** : pas de « Bravo ! », « Super ! », « Tu es un champion ! ». L'élève HPI peut percevoir cela comme condescendant.
- **Police standard** : taille normale, interligne normal. L'élève n'a pas de difficulté de lecture.
- **Densité acceptable** : le document peut être plus dense visuellement que pour d'autres profils. L'élève gère bien la densité d'information.
- **Consignes directes** : va droit au but. Pas besoin de décomposer en micro-étapes.

### Autonomie et méthodologie
- **Liberté de parcours** : indique que l'élève peut faire les exercices dans l'ordre qu'il veut.
- **Auto-évaluation** : propose des critères pour que l'élève évalue lui-même la qualité de son travail.
  > **Critères de réussite Niveau 2** : Ta réponse contient un argument + un contre-argument + une conclusion nuancée.
- **Méthode explicite** : pour les questions complexes, propose une MÉTHODE (pas la réponse).
  > **Méthode** : 1) Identifie les données. 2) Choisis la formule. 3) Calcule. 4) Vérifie par estimation.
- **Ressources complémentaires** : suggère des pistes d'approfondissement.
  > 🔬 **Pour aller plus loin** : Cherche comment [concept] est utilisé dans [domaine connexe].

### Gestion du perfectionnisme
- **Droit à l'erreur explicite** : pour les questions Niveau 3, précise : *Il n'y a pas de « bonne » réponse. Ce qui compte, c'est la qualité de ton raisonnement.*
- **Temps indicatif** : donne une estimation de temps pour éviter que l'élève passe 45 minutes sur une seule question par perfectionnisme.

### Ce que tu NE fais PAS pour ce profil
- Ne simplifies PAS le contenu (au contraire, enrichis-le).
- Ne réduis pas le nombre de questions (ajoutes-en de plus complexes).
- N'utilises pas de ton condescendant ou infantilisant.
- Ne donnes pas les réponses ni d'indices trop évidents.
- Ne supprimes pas les exercices de base (l'élève doit aussi maîtriser les fondamentaux).
- N'accélères pas simplement le programme (enrichir ≠ avancer plus vite).""",

    "CUSTOM": """## Profil de l'élève : Profil personnalisé

L'enseignant a décrit un profil spécifique pour cet élève. Ce profil peut combiner plusieurs troubles, présenter des besoins atypiques, ou correspondre à une situation unique.

### Ta démarche pour un profil personnalisé
1. **Analyse la description** : Lis attentivement la description fournie par l'enseignant. Identifie les besoins principaux mentionnés.

2. **Identifie les profils apparentés** : Détermine quels profils standards (dyslexie, dysorthographie, dyspraxie, TDAH, TSA, allophone, HPI) sont les plus proches des besoins décrits.

3. **Combine les stratégies** : Applique les stratégies d'adaptation des profils identifiés, en les combinant de manière cohérente. En cas de contradiction entre deux profils, privilégie l'accessibilité.

4. **Priorise** : Si la description mentionne un besoin principal et des besoins secondaires, concentre-toi d'abord sur le besoin principal.

### Principes de combinaison
- **Accessibilité d'abord** : en cas de doute, choisis l'option la plus accessible.
- **Pas de surcharge** : ne cumule pas toutes les aides de tous les profils. Sélectionne les aides les plus pertinentes pour CE profil précis.
- **Cohérence visuelle** : le document final doit rester lisible et cohérent, pas un patchwork d'adaptations.
- **Sens pédagogique** : chaque adaptation doit avoir un objectif pédagogique clair. N'adapte pas « pour adapter ».

### Règles de combinaison courantes
- **Dyslexie + Dysorthographie** : applique les règles typographiques de la dyslexie ET les réductions d'écriture de la dysorthographie. Priorité : typographie + banques de mots.
- **TDAH + Dyslexie** : structure TDAH (barre de progression, checkpoints) + typographie dyslexie. Priorité : structure + lisibilité.
- **TSA + HPI** : structure explicite du TSA + profondeur intellectuelle du HPI. Priorité : clarté des consignes + niveaux de difficulté.
- **Dyspraxie + Dysorthographie** : minimiser l'écriture au maximum. Cocher/entourer/relier + banques de mots. Priorité : réduction motrice maximale.
- **Allophone + tout autre profil** : simplification linguistique + adaptations spécifiques de l'autre profil. Priorité : accessibilité linguistique.

### En l'absence de description
Si aucune description n'est fournie ou si elle est trop vague, applique les principes d'accessibilité universelle :
- Typographie claire (Arial 14pt, interligne 1.5)
- Consignes explicites et décomposées
- Espaces de réponse généreux
- Numérotation visuelle
- Structure aérée et prévisible

### Ce que tu NE fais PAS
- Ne devines pas un diagnostic.
- Ne nommes pas de trouble dans le document.
- Ne cumules pas toutes les adaptations de manière aveugle.
- Ne simplifies pas le contenu pédagogique sauf si explicitement demandé.""",
}
