"""
Utility functions for mapping dog breed labels and extracting top predictions.
"""
import numpy as np

LABELS_DICT = {
    'Afghan_hound': 'Chart afgański',
    'African_hunting_dog': 'Likaon (pies dzikich)',
    'Airedale': 'Airedale terrier',
    'American_Staffordshire_terrier': 'Amerykański staffordshire terrier',
    'Appenzeller': 'Appenzeller (pies pasterski z Appenzell)',
    'Australian_terrier': 'Terrier australijski',
    'Bedlington_terrier': 'Bedlington terrier',
    'Bernese_mountain_dog': 'Berneński pies pasterski',
    'Blenheim_spaniel': 'Spaniel Blenheim',
    'Border_collie': 'Border collie',
    'Border_terrier': 'Border terrier',
    'Boston_bull': 'Boston terrier',
    'Bouvier_des_Flandres': 'Bouvier des Flandres (owczarek flandryjski)',
    'Brabancon_griffon': 'Griffon brabançon (gryf brukselski)',
    'Brittany_spaniel': 'Spaniel bretoński',
    'Cardigan': 'Welsh corgi cardigan',
    'Chesapeake_Bay_retriever': 'Chesapeake bay retriever',
    'Chihuahua': 'Chihuahua',
    'Dandie_Dinmont': 'Dandie dinmont terrier',
    'Doberman': 'Doberman',
    'English_foxhound': 'Angielski foxhound (ogar angielski)',
    'English_setter': 'Seter angielski',
    'English_springer': 'Springer spaniel angielski',
    'EntleBucher': 'Entlebucher (pies pasterski z Entlebuch)',
    'Eskimo_dog': 'Pies eskimoski',
    'French_bulldog': 'Buldog francuski',
    'German_shepherd': 'Owczarek niemiecki',
    'German_short-haired_pointer': 'Wyżeł niemiecki krótkowłosy',
    'Gordon_setter': 'Seter gordon',
    'Great_Dane': 'Dog niemiecki',
    'Great_Pyrenees': 'Pies górski Pirenejów',
    'Greater_Swiss_Mountain_dog': 'Wielki szwajcarski pies pasterski',
    'Ibizan_hound': 'Podenco ibicenco (chart z Ibizy)',
    'Irish_setter': 'Seter irlandzki',
    'Irish_terrier': 'Terrier irlandzki',
    'Irish_water_spaniel': 'Irlandzki spaniel wodny',
    'Irish_wolfhound': 'Wilczarz irlandzki',
    'Italian_greyhound': 'Chart włoski',
    'Japanese_spaniel': 'Spaniel japoński (chin japoński)',
    'Kerry_blue_terrier': 'Kerry blue terrier',
    'Labrador_retriever': 'Labrador retriever',
    'Lakeland_terrier': 'Lakeland terrier',
    'Leonberg': 'Leonberger',
    'Lhasa': 'Lhasa apso',
    'Maltese_dog': 'Maltańczyk',
    'Mexican_hairless': 'Xoloitzcuintle (pies meksykański bezwłosy)',
    'Newfoundland': 'Nowofundland',
    'Norfolk_terrier': 'Norfolk terrier',
    'Norwegian_elkhound': 'Elkhund norweski',
    'Norwich_terrier': 'Norwich terrier',
    'Old_English_sheepdog': 'Owczarek staroangielski (bobtail)',
    'Pekinese': 'Pekińczyk',
    'Pembroke': 'Welsh corgi pembroke',
    'Pomeranian': 'Szpic miniaturowy (pomeranian)',
    'Rhodesian_ridgeback': 'Rodezyjski ridgeback',
    'Rottweiler': 'Rottweiler',
    'Saint_Bernard': 'Bernardyn',
    'Saluki': 'Saluki (chart perski)',
    'Samoyed': 'Samoyed',
    'Scotch_terrier': 'Terier szkocki (scottish terrier)',
    'Scottish_deerhound': 'Deerhound szkocki (chart szkocki)',
    'Sealyham_terrier': 'Sealyham terrier',
    'Shetland_sheepdog': 'Owczarek szetlandzki (sheltie)',
    'Shih-Tzu': 'Shih tzu',
    'Siberian_husky': 'Husky syberyjski',
    'Staffordshire_bullterrier': 'Staffordshire bull terrier',
    'Sussex_spaniel': 'Sussex spaniel',
    'Tibetan_mastiff': 'Mastif tybetański',
    'Tibetan_terrier': 'Terrier tybetański',
    'Walker_hound': 'Walker hound (treeing walker coonhound)',
    'Weimaraner': 'Wyżeł weimarski',
    'Welsh_springer_spaniel': 'Springer spaniel walijski',
    'West_Highland_white_terrier': 'West highland white terrier',
    'Yorkshire_terrier': 'Yorkshire terrier',
    'affenpinscher': 'Affenpinscher',
    'basenji': 'Basenji',
    'basset': 'Basset',
    'beagle': 'Beagle',
    'black-and-tan_coonhound': 'Coonhound czarno-podpalany',
    'bloodhound': 'Bloodhound (ogar św. Huberta)',
    'bluetick': 'Bluetick coonhound',
    'borzoi': 'Chart rosyjski (borzoj)',
    'boxer': 'Bokser',
    'briard': 'Owczarek francuski długowłosy (briard)',
    'bull_mastiff': 'Bullmastiff',
    'cairn': 'Cairn terrier',
    'chow': 'Chow chow',
    'clumber': 'Clumber spaniel',
    'cocker_spaniel': 'Cocker spaniel',
    'collie': 'Collie',
    'curly-coated_retriever': 'Retriever kędzierzawy',
    'dhole': 'Dziki pies azjatycki (dhole)',
    'dingo': 'Dingo',
    'flat-coated_retriever': 'Retriever płasko umaszczony',
    'giant_schnauzer': 'Sznaucer olbrzymi',
    'golden_retriever': 'Golden retriever',
    'groenendael': 'Owczarek belgijski groenendael',
    'keeshond': 'Keeshond (wilczarz holenderski)',
    'kelpie': 'Kelpie australijski',
    'komondor': 'Komondor',
    'kuvasz': 'Kuvasz',
    'malamute': 'Malamute alaskański',
    'malinois': 'Owczarek belgijski malinois',
    'miniature_pinscher': 'Pinczer miniaturowy',
    'miniature_poodle': 'Pudel miniaturowy',
    'miniature_schnauzer': 'Sznaucer miniaturowy',
    'otterhound': 'Otterhound (ogar do wydr)',
    'papillon': 'Papillon (spaniel kontynentalny)',
    'pug': 'Mops',
    'redbone': 'Redbone coonhound',
    'schipperke': 'Schipperke',
    'silky_terrier': 'Silky terrier (terrier australijski jedwabisty)',
    'soft-coated_wheaten_terrier': 'Soft coated wheaten terrier (terrier pszeniczny)',
    'standard_poodle': 'Pudel królewski',
    'standard_schnauzer': 'Sznaucer średni',
    'toy_poodle': 'Pudel toy',
    'toy_terrier': 'Toy terrier',
    'vizsla': 'Wyżeł węgierski krótkowłosy (vizsla)',
    'whippet': 'Whippet',
    'wire-haired_fox_terrier': 'Terier foksa szorstkowłosy'
}
"""
Dictionary mapping Model dog breed labels to Dog CEO API format.
"""
LABELS_TO_API = {
    'Afghan_hound': 'hound afghan',
    'African_hunting_dog': 'african wild',
    'Airedale': 'airedale',
    'American_Staffordshire_terrier': 'terrier american',
    'Appenzeller': 'appenzeller',
    'Australian_terrier': 'terrier australian',
    'Bedlington_terrier': 'terrier bedlington',
    'Bernese_mountain_dog': 'mountain bernese',
    'Blenheim_spaniel': 'spaniel blenheim',
    'Border_collie': 'collie border',
    'Border_terrier': 'terrier border',
    'Boston_bull': 'bulldog boston',
    'Bouvier_des_Flandres': 'bouvier',
    'Brabancon_griffon': 'brabancon',
    'Brittany_spaniel': 'spaniel brittany',
    'Cardigan': 'corgi cardigan',
    'Chesapeake_Bay_retriever': 'retriever chesapeake',
    'Chihuahua': 'chihuahua',
    'Dandie_Dinmont': 'terrier dandie',
    'Doberman': 'doberman',
    'English_foxhound': 'hound english',
    'English_setter': 'setter english',
    'English_springer': 'springer english',
    'EntleBucher': 'entlebucher',
    'Eskimo_dog': 'eskimo',
    'French_bulldog': 'bulldog french',
    'German_shepherd': 'german shepherd',
    'German_short-haired_pointer': 'pointer german',
    'Gordon_setter': 'setter gordon',
    'Great_Dane': 'dane great',
    'Great_Pyrenees': 'pyrenees',
    'Greater_Swiss_Mountain_dog': 'mountain swiss',
    'Ibizan_hound': 'hound ibizan',
    'Irish_setter': 'setter irish',
    'Irish_terrier': 'terrier irish',
    'Irish_water_spaniel': 'spaniel irish',
    'Irish_wolfhound': 'wolfhound irish',
    'Italian_greyhound': 'greyhound italian',
    'Japanese_spaniel': 'spaniel japanese',
    'Kerry_blue_terrier': 'terrier kerryblue',
    'Labrador_retriever': 'labrador',
    'Lakeland_terrier': 'terrier lakeland',
    'Leonberg': 'leonberg',
    'Lhasa': 'lhasa',
    'Maltese_dog': 'maltese',
    'Mexican_hairless': 'mexicanhairless',
    'Newfoundland': 'newfoundland',
    'Norfolk_terrier': 'terrier norfolk',
    'Norwegian_elkhound': 'elkhound norwegian',
    'Norwich_terrier': 'terrier norwich',
    'Old_English_sheepdog': 'sheepdog english',
    'Pekinese': 'pekinese',
    'Pembroke': 'pembroke',
    'Pomeranian': 'pomeranian',
    'Rhodesian_ridgeback': 'ridgeback rhodesian',
    'Rottweiler': 'rottweiler',
    'Saint_Bernard': 'stbernard',
    'Saluki': 'saluki',
    'Samoyed': 'samoyed',
    'Scotch_terrier': 'terrier scottish',
    'Scottish_deerhound': 'deerhound scottish',
    'Sealyham_terrier': 'terrier sealyham',
    'Shetland_sheepdog': 'sheepdog shetland',
    'Shih-Tzu': 'shihtzu',
    'Siberian_husky': 'husky',
    'Staffordshire_bullterrier': 'bullterrier staffordshire',
    'Sussex_spaniel': 'spaniel sussex',
    'Tibetan_mastiff': 'mastiff tibetan',
    'Tibetan_terrier': 'terrier tibetan',
    'Walker_hound': 'hound walker',
    'Weimaraner': 'weimaraner',
    'Welsh_springer_spaniel': 'spaniel welsh',
    'West_Highland_white_terrier': 'terrier westhighland',
    'Yorkshire_terrier': 'terrier yorkshire',
    'affenpinscher': 'affenpinscher',
    'basenji': 'basenji',
    'basset': 'hound basset',
    'beagle': 'beagle',
    'black-and-tan_coonhound': 'coonhound',
    'bloodhound': 'hound blood',
    'bluetick': 'bluetick',
    'borzoi': 'borzoi',
    'boxer': 'boxer',
    'briard': 'briard',
    'bull_mastiff': 'mastiff bull',
    'cairn': 'terrier cairn',
    'chow': 'chow',
    'clumber': 'clumber',
    'cocker_spaniel': 'spaniel cocker',
    'collie': 'rough collie',
    'curly-coated_retriever': 'retriever curly',
    'dhole': 'dhole',
    'dingo': 'dingo',
    'flat-coated_retriever': 'retriever flatcoated',
    'giant_schnauzer': 'schnauzer giant',
    'golden_retriever': 'retriever golden',
    'groenendael': 'groenendael',
    'keeshond': 'keeshond',
    'kelpie': 'kelpie',
    'komondor': 'komondor',
    'kuvasz': 'kuvasz',
    'malamute': 'malamute',
    'malinois': 'malinois',
    'miniature_pinscher': 'pinscher miniature',
    'miniature_poodle': 'poodle miniature',
    'miniature_schnauzer': 'schnauzer miniature',
    'otterhound': 'otterhound',
    'papillon': 'papillon',
    'pug': 'pug',
    'redbone': 'redbone',
    'schipperke': 'schipperke',
    'silky_terrier': 'terrier silky',
    'soft-coated_wheaten_terrier': 'terrier wheaten',
    'standard_poodle': 'poodle standard',
    'standard_schnauzer': 'none',
    'toy_poodle': 'poodle toy',
    'toy_terrier': 'terrier toy',
    'vizsla': 'vizsla',
    'whippet': 'whippet',
    'wire-haired_fox_terrier': 'terrier fox'
}


def get_top3_labels_with_conf(results, labels_map=None):
    """
    Extract the top 3 labels with the highest confidence from model results.
    :param results: list of model prediction results
    :param labels_map:
    :return: list of top 3 dicts for labels,confidence based on confidence
    """
    result0 = results[0]
    if len(result0.boxes) == 0:
        return []

    class_indices = result0.boxes.cls.cpu().numpy().astype(int)
    confidences = result0.boxes.conf.cpu().numpy()

    sorted_idx = np.argsort(confidences)[::-1]
    top3_idx = sorted_idx[:3]

    top3 = []
    for i in top3_idx:
        label = result0.names[class_indices[i]]
        if labels_map:
            label = labels_map.get(label, label)
        top3.append({'label': label, 'confidence': float(confidences[i])})

    return top3


def get_label_and_conf(result):
    """
    Extract the top label and its confidence from a single model result.
    :param result: single model prediction result
    :return:
    """
    if result.boxes is None or len(result.boxes) == 0:
        return None
    cls = int(result.boxes.cls[0].item())
    conf = float(result.boxes.conf[0].item())

    label = result.names[cls]

    return {'label': map_label_to_polish(label), 'confidence': conf}


def map_label_to_polish(label: str) -> str:
    """
    Map an English dog breed label to its Polish equivalent.
    :param label: English dog breed label
    :return: Polish dog breed label
    """
    return LABELS_DICT.get(label, label)


def map_label_to_api(label: str) -> str:
    """
    Map a dog breed label to the format used by the Dog CEO API.
    :param label: Dog breed label
    :return: Formatted label for Dog CEO API
    """
    return LABELS_TO_API.get(label, label)


def get_all_breeds():
    """
    Get the dictionary of all dog breeds with their Polish equivalents.
    :return:
    """
    return LABELS_DICT
