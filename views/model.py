"""
Model information view for the PsiLook app.
"""
import streamlit as st


def get_model_page():
    """
    Pobierz informacje o aktualnie załadowanym modelu.
    :return: tekst z informacjami o modelu
    """
    st.title("Informacje o modelu")
    with st.expander("Informacje o modelu"):
        st.write("""
        Ta sekcja zawiera szczegóły dotyczące aktualnie załadowanego modelu uczenia maszynowego 
        używanego do rozpoznawania ras psów.

        - **Typ modelu**: YOLO (You Only Look Once)
        - **Wersja**: YOLOv11n 
        - **Dane treningowe**: Zbiór danych Stanford Dogs Dataset, zawierający ponad 20 000 obrazów 
        przedstawiających 120 różnych ras psów. 
        
        (https://universe.roboflow.com/iliescu-mihail-doirn/stanford-dogs-dataset-dog-breed)
        - **Wydajność**: Wysoka dokładność w wykrywaniu i klasyfikacji ras psów w czasie rzeczywistym.
        """)
    with st.expander("Architektura modelu"):
        st.markdown("""
        **YOLO11n** – szybka detekcja obiektów oparta na sieciach konwolucyjnych (CNN)

        **YOLO11n** to nano‑wariant najnowszej generacji modeli YOLO (You Only Look Once), zoptymalizowany 
        pod kątem **szybkości i niskich zasobów** – idealny na urządzenia edge.
        
        **Z czego się składa?**
        
        - **Backbone** – wydobywa cechy z obrazu przy użyciu lekkich bloków **C3k2**.
        - **SPPF** – łączy informacje z różnych skal obrazu, pozwalając wykrywać małe i duże obiekty.
        - **C2PSA** – mechanizm uwagi przestrzennej, który lepiej skupia się na ważnych regionach.
        - **Neck** – łączy cechy z różnych poziomów (FPN + PAN‑like).
        - **Head** – przewiduje klasy, pewność obiektu i bounding boxy, dla różnych skal obiektów.
        
        **Dlaczego „nano”?**
        
        - Niewielka liczba parametrów (~2.6M), bardzo szybki (~1.5–3 ms na GPU).
        - Zachowuje multi-scale detection (małe/średnie/duże obiekty).
        - Idealny dla real-time i urządzeń z ograniczonymi zasobami.
        
        """)
    with st.expander("Training modelu"):
        st.write("""Model został wytrenowany na zbiorze danych Stanford Dogs Dataset, 
        który zawiera ponad 20 000
        obrazów przedstawiających 120 różnych ras psów. Dane zostały pobrane z serwisu Roboflow.""")
        st.write("""**Link do zbioru danych:**  
        (https://universe.roboflow.com/iliescu-mihail-doirn/stanford-dogs-dataset-dog-breed)""")
        st.write("""**Proces trenowania modelu obejmował następujące kroki:**""")
        st.write("""
        1. **Przygotowanie danych**: Pobrane dane z Roboflow były już oznaczone i podzielone na 
        zestawy treningowe i walidacyjne.
        2. **Uczenie modelu**: Do uczenia modelu użyto Google Colab z GPU oraz frameworku Ultralytics.
         Model trenowano przez 60 epok z użyciem domyślnych hiperparametrów YOLO11n.
        3. **Ewaluacja**: Po zakończeniu treningu model został oceniony pod kątem dokładności i
         zdolności do generalizacji na zestawie walidacyjnym.
        """)
        st.write("""**Metryki dotyczące wydajności modelu po treningu:**""")
        st.write("""
        - **Dokładność wykrywania obiektów (mAP50)**: 77.9%
        - **Dokładność wykrywania obiektów (mAP50-95)**: 68.7%
        - **Precyzja (P)**: 73.6%
        - **Czułość (R)**: 71.0%""")

        st.markdown("""**Log z ostatniej epoki treningu:**""")
        st.write("""```
        Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
        60/60      3.45G     0.3742     0.6766      1.061          2        640: 100% ━━━━━━━━━━━━ 897/897 3.8it/s 3:55
        Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 97/97 4.0it/s 24.3s
        all       3086       3328      0.736       0.71      0.779      0.687""")

        st.markdown("""**Podsumowanie modelu po treningu:**""")
        st.write("""```
        YOLO11n summary (fused): 100 layers, 2,653,648 parameters, 0 gradients, 6.7 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 97/97 3.8it/s 25.3s
                   all       3086       3328      0.737       0.71      0.779      0.687
          Afghan_hound         38         54      0.975      0.907      0.963      0.877
   African_hunting_dog         27         34      0.839      0.768      0.892      0.762
              Airedale         30         32      0.732      0.855      0.903      0.848
American_Staffordshire_terrier         18         18      0.344      0.389      0.321      0.261
           Appenzeller         17         20       0.42        0.6      0.615      0.497
    Australian_terrier         28         29       0.48      0.483      0.594      0.544
    Bedlington_terrier         24         26      0.705      0.731      0.802      0.688
  Bernese_mountain_dog         42         44      0.931       0.92      0.962       0.84
      Blenheim_spaniel         28         29       0.89      0.862      0.952      0.858
         Border_collie         26         27      0.719      0.667      0.694      0.624
        Border_terrier         28         28       0.78      0.884      0.903      0.838
           Boston_bull         33         36      0.736      0.833      0.815      0.638
  Bouvier_des_Flandres         23         24      0.819      0.756      0.858      0.805
     Brabancon_griffon         19         19      0.922      0.842      0.918       0.86
      Brittany_spaniel         21         21      0.735      0.667      0.754       0.68
              Cardigan         21         24      0.717      0.667      0.776      0.723
Chesapeake_Bay_retriever         34         36      0.745      0.806      0.837      0.724
             Chihuahua         26         28      0.691      0.399      0.595      0.478
        Dandie_Dinmont         24         27      0.839      0.667      0.861      0.796
              Doberman         29         32      0.753      0.667      0.828      0.731
      English_foxhound         23         28      0.622      0.429      0.644      0.561
        English_setter         19         22      0.822      0.631      0.817      0.696
      English_springer         18         19      0.816      0.895      0.914      0.819
           EntleBucher         28         32      0.565      0.594      0.676       0.58
            Eskimo_dog         22         26      0.377      0.269      0.454      0.404
        French_bulldog         23         24      0.641      0.744      0.702      0.672
       German_shepherd         25         25      0.847       0.76      0.834      0.766
German_short-haired_pointer         17         17      0.774      0.882      0.928      0.889
         Gordon_setter         28         30       0.95        0.9      0.944      0.807
            Great_Dane         22         23       0.42      0.478      0.463      0.423
        Great_Pyrenees         38         41      0.776      0.683      0.799      0.669
Greater_Swiss_Mountain_dog         35         40      0.848      0.698      0.859      0.714
          Ibizan_hound         26         29      0.913      0.722      0.816      0.754
          Irish_setter         26         30      0.809      0.767      0.875      0.771
         Irish_terrier         18         20      0.656        0.7      0.773      0.706
   Irish_water_spaniel         21         22      0.784      0.955      0.925      0.836
       Irish_wolfhound         39         44      0.574      0.614      0.672      0.568
     Italian_greyhound         24         29      0.639      0.483      0.673      0.519
      Japanese_spaniel         29         33      0.753       0.83      0.868      0.721
    Kerry_blue_terrier         19         20      0.752        0.8      0.839      0.803
    Labrador_retriever         32         37      0.813       0.73      0.874      0.787
      Lakeland_terrier         30         31      0.723      0.673      0.674       0.62
              Leonberg         29         31      0.832      0.935      0.952      0.873
                 Lhasa         31         32      0.599      0.531      0.594      0.524
           Maltese_dog         45         46      0.828      0.838      0.914      0.798
      Mexican_hairless         17         18      0.743      0.722      0.861       0.79
          Newfoundland         24         25       0.77       0.68      0.765      0.592
       Norfolk_terrier         31         32      0.712      0.594      0.642      0.576
    Norwegian_elkhound         37         39      0.851      0.821      0.911      0.844
       Norwich_terrier         27         34      0.611      0.706       0.71      0.661
  Old_English_sheepdog         26         28      0.773      0.821      0.865      0.779
              Pekinese         19         19        0.7      0.789      0.763      0.619
              Pembroke         27         28        0.9      0.964      0.974      0.856
            Pomeranian         28         28      0.929      0.937      0.965      0.832
   Rhodesian_ridgeback         24         25      0.522        0.4      0.531      0.474
            Rottweiler         16         16      0.718      0.938      0.741       0.68
         Saint_Bernard         23         24      0.892      0.917      0.969      0.886
                Saluki         21         23      0.772      0.735      0.794      0.709
               Samoyed         24         29      0.737      0.897      0.881      0.792
        Scotch_terrier         20         22      0.755      0.864      0.926      0.866
    Scottish_deerhound         30         32      0.703      0.844      0.777      0.728
      Sealyham_terrier         37         41      0.939      0.927      0.974      0.859
     Shetland_sheepdog         18         20      0.728      0.804      0.796      0.667
              Shih-Tzu         26         31      0.627      0.705      0.768      0.587
        Siberian_husky         32         35      0.472      0.343      0.507      0.435
Staffordshire_bullterrier         21         22      0.861      0.591       0.77      0.712
        Sussex_spaniel         27         27      0.829      0.895      0.932      0.852
       Tibetan_mastiff         21         22        0.9      0.909      0.944      0.817
       Tibetan_terrier         42         44      0.799      0.659      0.752      0.653
          Walker_hound         19         21      0.462      0.381      0.572      0.468
            Weimaraner         24         25      0.942       0.76      0.922      0.797
Welsh_springer_spaniel         28         29      0.793       0.66      0.819      0.684
West_Highland_white_terrier         20         21      0.747       0.81      0.838      0.746
     Yorkshire_terrier         20         20      0.657       0.55      0.626      0.561
         affenpinscher         26         26      0.737      0.808      0.805      0.722
               basenji         26         29      0.675      0.621      0.723      0.573
                basset         29         30       0.71      0.767      0.629      0.501
                beagle         29         31      0.644      0.645      0.701      0.608
black-and-tan_coonhound         27         27      0.822      0.852      0.893      0.835
            bloodhound         29         29      0.757      0.724       0.81       0.74
              bluetick         30         30      0.849        0.7       0.83      0.729
                borzoi         22         23      0.855      0.652      0.846      0.806
                 boxer         30         30       0.86        0.5      0.744       0.61
                briard         13         14      0.519      0.714      0.747      0.688
          bull_mastiff         31         39      0.809      0.846       0.87      0.761
                 cairn         36         39      0.823      0.692      0.844      0.722
                  chow         32         33      0.903      0.879      0.886      0.824
               clumber         22         25      0.897       0.84      0.907      0.693
        cocker_spaniel         28         28      0.852      0.607      0.679       0.63
                collie         22         28      0.788        0.4      0.582      0.431
curly-coated_retriever         20         22      0.868      0.727      0.871      0.788
                 dhole         24         28      0.784      0.777      0.852      0.689
                 dingo         29         32      0.715      0.706      0.789      0.731
 flat-coated_retriever         25         25      0.687       0.76      0.817      0.697
       giant_schnauzer         32         35      0.725      0.679      0.758       0.69
      golden_retriever         30         32      0.801      0.755      0.812      0.731
           groenendael         15         15      0.784      0.933      0.916       0.89
              keeshond         25         28      0.999      0.964      0.968      0.839
                kelpie         18         18      0.648      0.556      0.649      0.624
              komondor         23         26      0.954      0.808      0.886      0.728
                kuvasz         23         24      0.678      0.702      0.757      0.676
              malamute         21         23      0.374      0.442      0.481      0.444
              malinois         21         21      0.676       0.81      0.807      0.673
    miniature_pinscher         33         34      0.818      0.796      0.857      0.792
      miniature_poodle         17         18      0.481      0.413      0.499      0.403
   miniature_schnauzer         25         27      0.694      0.593      0.669      0.599
            otterhound         20         22      0.946      0.591      0.775      0.688
              papillon         25         25      0.922       0.95      0.976      0.859
                   pug         38         38       0.82      0.816      0.865      0.689
               redbone         21         21      0.567      0.623      0.606      0.533
            schipperke         17         19      0.797      0.789      0.863      0.733
         silky_terrier         25         26        0.7      0.615      0.802      0.735
soft-coated_wheaten_terrier         26         26      0.604      0.615      0.657      0.582
       standard_poodle         28         30      0.508        0.3      0.489      0.425
    standard_schnauzer         18         22      0.389      0.364      0.492      0.413
            toy_poodle         19         19      0.506      0.737      0.637      0.594
           toy_terrier         25         25      0.746      0.703      0.776      0.709
                vizsla         22         22      0.573      0.545      0.538      0.457
               whippet         31         39      0.556      0.538      0.595      0.486
wire-haired_fox_terrier         26         26      0.871      0.769      0.894      0.826""")
