# -------------------------------------------------------------------------
# FICHIER: systeme_navigation.rpy
# -------------------------------------------------------------------------

# 1. DÉFINITION DE LA LOGIQUE (Modèle)
# Ce bloc s'exécute au lancement du jeu, avant même le menu principal.
init python:
    class NavigationState:
        def __init__(self):
            self.current_location = "start"
            self.previous_location = None
            self.clock = 0 
            
        def travel(self, destination):
            """
            1. Met à jour l'état (Mémoire).
            2. Calcule la destination dynamique (Logique).
            3. Provoque le saut immédiat (Action).
            """
            # --- PHASE 1 : Mise à jour de l'état (State Update) ---
            self.previous_location = self.current_location
            self.current_location = destination
            self.clock += 1
            
            # --- PHASE 2 : Résolution de la topologie (Routing) ---
            target_label = self._resolve_label()
            
            # --- PHASE 3 : Exécution du saut (Dispatch) ---
            # renpy.jump interrompt l'exécution courante et va au label.
            renpy.jump(target_label)

        def _resolve_label(self):
            """
            Méthode interne (privée) pour déterminer le label cible.
            """
            # 1. Essai : Cas spécifique (ex: loc_B_from_A)
            if self.previous_location:
                specific_label = "loc_{}_from_{}".format(self.current_location, self.previous_location)
                if renpy.has_label(specific_label):
                    return specific_label
            
            # 2. Essai : Cas par défaut du lieu (ex: loc_B_default)
            default_label = "loc_{}_default".format(self.current_location)
            if renpy.has_label(default_label):
                return default_label
            
            # 3. Sécurité : Si même le défaut n'existe pas
            return "error_missing_location_label"

# Instanciation
default nav_manager = NavigationState()

# Label de sécurité technique (au cas où vous oubliez de créer le label)
label error_missing_location_label:
    "ERREUR SYSTEME : Le lieu demandé n'a pas de label défini (ni spécifique, ni défaut)."
    $ renpy.full_restart()

