
class CinematiqueMortController:
    def __init__(self):
    
        pass
        
    def retry_level(self,screen,level_id):
        from Niveau import Niveau
        # Importer Niveau ici pour éviter l'importation circulaire
        
        # Créer et lancer le niveau
        niveau = Niveau(screen,70,40,60,f"images\lv{level_id}_background.png",f"musique\musique_lvl{level_id}.mp3",level_id)
        niveau.run()

    
