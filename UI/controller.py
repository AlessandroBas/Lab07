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
        return [ft.dropdown.Option("Nessun Filtro")] + [ft.dropdown.Option(m.nome) for m in musei]

    def popola_dropdown_epoca(self):
        epoche = self._model.get_epoche()
        return [ft.dropdown.Option("Nessun Filtro")] + [ft.dropdown.Option(e[0]) for e in epoche]

    # CALLBACKS DROPDOWN
    # TODO
    def handler_dropdown_change_museo(self, e):
        if self.museo_selezionato is None:
            self.museo_selezionato = self._view.filtro_museo.value
        else:
         self.handler_btn_artefatti(None)

    def handler_dropdown_change_epoca(self, e):
        if self.epoca_selezionata is None:
            self.epoca_selezionata = self._view.filtro_epoca.value
        else:
            self.handler_btn_artefatti(None)

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def handler_btn_artefatti(self,e):
        self._view.lista_artefatti.clean()
        if self.museo_selezionato is not None and self.epoca_selezionata is not None:
            artefatti=self._model.get_artefatti_filtrati(self.museo_selezionato,self.epoca_selezionata)
            if not artefatti:
                self._view.lista_artefatti.controls.append(ft.Text("Nessun artefatto trovato."))
            else:
                 for a in artefatti:
                    self._view.lista_artefatti.controls.append(ft.Text(str(a)))
        else:
            self._view.show_alert("Devi inserire un Museo e/o un Epoca")
        self._view.update()
