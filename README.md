# Algoritmi della PNL

Questa cartella contiene tutto il necessario per risolvere (quasi tutto) l'Esercizio 4 del compito, focalizzandosi sulla parte di **Frank-Wolfe** e **Gradiente Proiettato**.

## Requisiti

Per eseguire il codice, assicurarsi di avere Python installato sul proprio sistema. Successivamente, aprire il terminale nella cartella scaricata ed eseguire il seguente comando:

```bash
pip install -r requirements.txt
```

## Istruzioni

1. **Estrarre la cartella Utilities e aprire il file principale:**
   - Estrarre la cartella `Utilities.zip`
   - Utilizzare VS Code (o un editor compatibile con Colorama) per aprire il file `Ex. 4.py`.

3. **Eseguire l'Esercizio 4:**
   - Il file `Ex. 4.py` combina tutte le funzionalità necessarie per risolvere l'esercizio.
   - Seguire le istruzioni a schermo per inserire la funzione, il punto iniziale e i vincoli.

4. **Uso delle funzioni singole:**
   - Tutte le funzioni utilizzate per risolvere l'Esercizio 4 sono organizzate nella cartella `Utilities`.
   - È possibile utilizzare ogni funzione separatamente importandola nei propri script.

## File Aggiuntivi

Oltre a `Ex. 4.py`, sono disponibili due file opzionali per l'ottimizzazione senza vincoli:

- **`Algorithms for unconstrained max.py`:**
  - Contiene implementazioni di:
    - Metodo del gradiente libero a passo costante.
    - Metodo del gradiente libero a passo ideale.
    - Metodo di Newton.
    - Metodo di Armijo-Goldstein-Wolfe.

- **`Algorithms for unconstrained min.py`:**
  - Contiene gli stessi metodi, ma per la minimizzazione senza vincoli.

**Nota:** È improbabile che questi algoritmi siano richiesti nel compito scritto, ma sono inclusi per completezza.

## Struttura della Cartella

- `Ex. 4.py`: File principale che combina tutte le funzionalità.
- `Utilities/`: Contiene le implementazioni delle funzioni necessarie per Frank-Wolfe e Gradiente Proiettato.
- `Algorithms for unconstrained max.py`: Algoritmi per massimizzazione senza vincoli.
- `Algorithms for unconstrained min.py`: Algoritmi per minimizzazione senza vincoli.
- `requirements.txt`: Elenco delle dipendenze necessarie.

---
