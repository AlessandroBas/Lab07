import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown_museo(self):
        musei = self._model.get_musei()
        opzioni = [ft.dropdown.Option(text=m.nome, key=m.id) for m in musei]
        return opzioni

    def popola_dropdown_epoca(self):
        epoche = self._model.get_epoche()
        opzioni = [ft.dropdown.Option(text=e, key=e) for e in epoche]
        return opzioni

    # CALLBACKS DROPDOWN
    # TODO
    def handler_dropdown_change(self, e):
        self.selected_id =self._view.filtro_museo.value
        musei = self._model.get_musei()
        self.museo_selezionato = next((m for m in musei if str(m.id) == str(self.selected_id)), None)

        self.epoca_selezionata = self._view.filtro_epoca.value
        if self.selected_id :
            self.selected_id=str(int(self.selected_id)-14)
        print(f"Museo selezionato: {self.museo_selezionato}")
        print(f"Epoca selezionata: {self.epoca_selezionata}")

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def handler_btn_artefatti(self,e):
        self._view.lista_artefatti.clean()
        artefatti=self._model.get_artefatti_filtrati(self.selected_id,self.epoca_selezionata)

        if not artefatti:
            self._view.lista_artefatti.controls.append(ft.Text("Nessun artefatto trovato."))
        else:
            for a in artefatti:
                self._view.lista_artefatti.controls.append(ft.Text(str(a)))
            print(self._view.lista_artefatti)
        self._view.update()
