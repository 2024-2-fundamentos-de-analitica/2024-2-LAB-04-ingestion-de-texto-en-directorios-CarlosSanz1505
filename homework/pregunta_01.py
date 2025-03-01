# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import os
    import shutil
    import glob
    import pandas as pd

    # Restablecer el estado del directorio files antes de ejecutar
    if os.path.exists('./files/output'):
        shutil.rmtree('./files/output')

    # estructuras de los archivos de salida
    columns = ['phrase', 'target']
    output = {
        'train': pd.DataFrame(columns=columns),
        'test': pd.DataFrame(columns=columns)
    }
    
    # Recorrer y leer archivos de entrada
    for pathname in glob.glob('./files/input/*/*/*.txt'):
        pathname = pathname.replace('\\', '/')
        print(pathname)
        with open(pathname) as file:
            phrase = file.read()
            split, target = os.path.dirname(pathname).split('/')[-2:]
            values = pd.DataFrame([[phrase, target]], columns=columns)
            output[split] = pd.concat([output[split], values], ignore_index=True)

    # Generar archivos de salida
    os.makedirs('./files/output/')
    for split in output:
        output[split].to_csv(f'./files/output/{split}_dataset.csv')
pregunta_01()