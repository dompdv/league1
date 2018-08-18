def account_for_2018_results(matches):
    results = [
        # num match, FTHG, FTAG, Prono, s1, s2
        # Première journée
        (0, 3, 4, 1, 1, 0),
        (1, 0, 2, 1, 3, 1),
        (2, 3, 1, 2, 0, 1),
        (3, 2, 0, 1, 3, 0),
        (4, 4, 0, 1, 2, 0),
        (5, 1, 2, 1, 2, 1),
        (6, 1, 3, 2, 0, 1),
        (7, 0, 1, 1, 1, 0),
        (8, 3, 0, 1, 2, 0),
        (9, 2, 1, 1, 1, 0),
    ]

    for num, fthg, ftag, prono, exact_s1, exact_s2 in results:
        matches[num]['Played'] = True
        matches[num]['FTHG'] = fthg
        matches[num]['FTAG'] = ftag
        matches[num]['Prono'] = prono
        matches[num]['Exact_s1'] = exact_s1
        matches[num]['Exact_s2'] = exact_s2
    return matches

'''
for season in [2015,2016,2017]:

Team                  |  #  |   |  0   |   1   |   2   |   3   | Total |Avg A|    |  0   |   1   |   2   |   3   | Total|Avg D |
       Ajaccio        |  0  | A | 25   |  25   |  25   |  25   | 100  | 1.5  |  D | 25   |  25   |  25   |  25   | 100  | 1.5  |
     Ajaccio GFCO     |  1  | A | 93   |   4   |   2   |   2   | 100  | 0.1  |  D | 93   |   3   |   2   |   1   | 100  | 0.1  |
        Amiens        |  2  | A | 65   |  31   |   2   |   2   | 100  | 0.4  |  D |  2   |   2   |   2   |  95   | 100  | 2.9  |
        Angers        |  3  | A |  1   |  96   |   1   |   1   | 100  | 1.0  |  D |  1   |   1   |  97   |   1   | 100  | 2.0  |
       Auxerre        |  4  | A | 25   |  25   |  25   |  25   | 100  | 1.5  |  D | 25   |  25   |  25   |  25   | 100  | 1.5  |
        Bastia        |  5  | A | 93   |   2   |   2   |   2   | 100  | 0.1  |  D |  2   |  95   |   2   |   1   | 100  | 1.0  |
       Bordeaux       |  6  | A |  1   |   1   |  95   |   3   | 100  | 2.0  |  D |  1   |   1   |  97   |   1   | 100  | 2.0  |
        Brest         |  7  | A | 25   |  25   |  25   |  25   | 100  | 1.5  |  D | 25   |  25   |  25   |  25   | 100  | 1.5  |
         Caen         |  8  | A | 90   |   6   |   2   |   2   | 100  | 0.2  |  D | 75   |   5   |  20   |   1   | 100  | 0.5  |
        Dijon         |  9  | A |  1   |   1   |  50   |  48   | 100  | 2.4  |  D | 95   |   2   |   2   |   1   | 100  | 0.1  |
Evian Thonon Gaillard | 10  | A | 25   |  25   |  25   |  25   | 100  | 1.5  |  D | 25   |  25   |  25   |  25   | 100  | 1.5  |
       Guingamp       | 11  | A |  2   |  47   |  50   |   1   | 100  | 1.5  |  D |  1   |  95   |   2   |   1   | 100  | 1.0  |
         Lens         | 12  | A | 25   |  25   |  25   |  25   | 100  | 1.5  |  D | 25   |  25   |  25   |  25   | 100  | 1.5  |
        Lille         | 13  | A |  4   |   4   |  89   |   3   | 100  | 1.9  |  D | 34   |   2   |   2   |  62   | 100  | 1.9  |
       Lorient        | 14  | A |  4   |  94   |   1   |   1   | 100  | 1.0  |  D | 86   |   3   |   9   |   1   | 100  | 0.3  |
         Lyon         | 15  | A |  1   |   1   |   1   |  97   | 100  | 2.9  |  D | 21   |   1   |   1   |  77   | 100  | 2.3  |
      Marseille       | 16  | A |  1   |   1   |   1   |  97   | 100  | 2.9  |  D |  1   |   1   |   1   |  97   | 100  | 2.9  |
         Metz         | 17  | A | 96   |   2   |   1   |   1   | 100  | 0.1  |  D | 97   |   1   |   1   |   1   | 100  | 0.1  |
        Monaco        | 18  | A |  1   |   1   |   1   |  96   | 100  | 2.9  |  D |  1   |   1   |   1   |  97   | 100  | 2.9  |
     Montpellier      | 19  | A |  7   |   2   |   3   |  87   | 100  | 2.7  |  D |  4   |  48   |  44   |   4   | 100  | 1.5  |
        Nancy         | 20  | A | 81   |   8   |   8   |   3   | 100  | 0.3  |  D | 10   |  86   |   2   |   2   | 100  | 1.0  |
        Nantes        | 21  | A | 96   |   1   |   1   |   1   | 100  | 0.1  |  D |  1   |   1   |  97   |   1   | 100  | 2.0  |
         Nice         | 22  | A |  2   |   3   |  79   |  16   | 100  | 2.1  |  D | 32   |  11   |  55   |   2   | 100  | 1.3  |
       Paris SG       | 23  | A |  2   |   2   |   2   |  93   | 100  | 2.9  |  D |  4   |   4   |   4   |  88   | 100  | 2.8  |
        Reims         | 24  | A |  7   |  24   |  67   |   3   | 100  | 1.7  |  D |  2   |  82   |   7   |   8   | 100  | 1.2  |
        Rennes        | 25  | A |  2   |  17   |  63   |  18   | 100  | 2.0  |  D |  4   |   6   |  86   |   4   | 100  | 1.9  |
       Sochaux        | 26  | A | 25   |  25   |  25   |  25   | 100  | 1.5  |  D | 25   |  25   |  25   |  25   | 100  | 1.5  |
      St Etienne      | 27  | A |  3   |   3   |  83   |  11   | 100  | 2.0  |  D |  2   |   5   |  83   |  10   | 100  | 2.0  |
      Strasbourg      | 28  | A |  2   |  96   |   1   |   1   | 100  | 1.0  |  D | 96   |   2   |   2   |   1   | 100  | 0.1  |
       Toulouse       | 29  | A |  3   |  52   |  39   |   6   | 100  | 1.5  |  D |  1   |  96   |   1   |   1   | 100  | 1.0  |
        Troyes        | 30  | A | 25   |   2   |  36   |  38   | 100  | 1.9  |  D | 92   |   3   |   2   |   3   | 100  | 0.2  |
     Valenciennes     | 31  | A | 25   |  25   |  25   |  25   | 100  | 1.5  |  D | 25   |  25   |  25   |  25   | 100  | 1.5  |
        Nîmes         | 32  | A | 25   |  25   |  25   |  25   | 100  | 1.5  |  D | 25   |  25   |  25   |  25   | 100  | 1.5  |

'''
def attack_defense_vectors():
    attack_vector = [
        [0.25, 0.25, 0.25, 0.25],
        [0.9258352368526939, 0.03756123482806049, 0.019093574621211553, 0.017509953698034268],
        [0.6525239663806713, 0.31121738321999354, 0.017477059066055622, 0.018781591333279505],
        [0.009801042663026671, 0.9626764812981248, 0.012943197270637892, 0.014579278768210606],
        [0.25, 0.25, 0.25, 0.25],
        [0.9335459476483825, 0.02355384041568731, 0.02362209359420889, 0.019278118341721173],
        [0.010849860820036493, 0.011687611724855398, 0.9478239852363747, 0.029638542218733268],
        [0.25, 0.25, 0.25, 0.25],
        [0.9029414374212845, 0.05910357265841739, 0.01871339237357616, 0.019241597546722007],
        [0.009808659135770939, 0.010077545519228176, 0.5005362127834514, 0.4795775825615497],
        [0.25, 0.25, 0.25, 0.25],
        [0.020596610799291096, 0.4669971062767843, 0.5024450323156865, 0.009961250608238041],
        [0.25, 0.25, 0.25, 0.25],
        [0.03620025279455835, 0.04284538012928184, 0.8902480739216428, 0.03070629315451695],
        [0.03801157900298658, 0.9373040283938983, 0.012557430745260476, 0.012126961857854819],
        [0.01024344885533825, 0.010840267145938887, 0.01304362018492344, 0.9658726638137994],
        [0.009701340424118339, 0.00970059323558949, 0.010009901334247027, 0.9705881650060452],
        [0.9646765176949241, 0.01553164632598049, 0.009898074116784268, 0.009893761862311053],
        [0.010421370952837213, 0.010607721754654346, 0.01429010062103444, 0.964680806671474],
        [0.07161607975304426, 0.019609247137244896, 0.03451556189192686, 0.8742591112177841],
        [0.8120527964135668, 0.07819838015251769, 0.0768091844697132, 0.032939638964202586],
        [0.9643142103113882, 0.009984576697062719, 0.013269791327675324, 0.012431421663873695],
        [0.024956548358870304, 0.03375176475900788, 0.7861228425655831, 0.15516884431653877],
        [0.024393509046498292, 0.01811798656540713, 0.02308369141439509, 0.9344048129736995],
        [0.06715478120580222, 0.23542282319825103, 0.6658784334166165, 0.031543962179330226],
        [0.02305355918945892, 0.1671216263818863, 0.6344522531643927, 0.17537256126426204],
        [0.25, 0.25, 0.25, 0.25],
        [0.03166765342586798, 0.027429387138621895, 0.827323804650578, 0.11357915478493213],
        [0.022783014655679484, 0.9574471142106569, 0.009836025293879213, 0.009933845839784622],
        [0.03382071467886287, 0.5191785647435507, 0.3855632313599131, 0.061437489217673384],
        [0.24952103672710318, 0.01752023926307575, 0.3574882907560001, 0.375470433253821],
        [0.25, 0.25, 0.25, 0.25],
        [0.25, 0.25, 0.25, 0.25],
    ]
    defense_vector = [
        [0.25, 0.25, 0.25, 0.25],
        [0.9288818273674078, 0.03407443821586152, 0.022167100044681975, 0.014876634372048609],
        [0.01553409106106356, 0.01742795911342955, 0.01800067116377123, 0.9490372786617357],
        [0.009815661501607276, 0.009904294970580214, 0.9706155785283834, 0.009664464999429068],
        [0.25, 0.25, 0.25, 0.25],
        [0.018555093145821253, 0.9530926818873529, 0.01797688288372391, 0.010375342083101787],
        [0.011133398486899534, 0.010369736420562874, 0.9684157035555858, 0.0100811615369517],
        [0.25, 0.25, 0.25, 0.25],
        [0.7478568211071579, 0.045194250461668244, 0.19649901730588556, 0.01044991112528831],
        [0.9543623288856059, 0.01651086205488383, 0.016811903833066865, 0.012314905226443304],
        [0.25, 0.25, 0.25, 0.25],
        [0.01342526315735859, 0.95343057972595, 0.021899567649215804, 0.011244589467475431],
        [0.25, 0.25, 0.25, 0.25],
        [0.3427040731264762, 0.01626440637911252, 0.021266924780940385, 0.619764595713471],
        [0.858810153066881, 0.0347019072540603, 0.09227418219986656, 0.014213757479192096],
        [0.21113467186588483, 0.01037930247622747, 0.010192517417983831, 0.7682935082399038],
        [0.009791244144416508, 0.010196915696996267, 0.010216745290307014, 0.9697950948682803],
        [0.9696111755421495, 0.01060247890284621, 0.009897206310624606, 0.009889139244379902],
        [0.009873648496277384, 0.010545486805498822, 0.01041251633486049, 0.9691683483633633],
        [0.04436985203544202, 0.47823650387595656, 0.4398404210920957, 0.03755322299650569],
        [0.09647302653007765, 0.8623961942757232, 0.016833763516018965, 0.02429701567818019],
        [0.011765819131064064, 0.010822412002548602, 0.9677234810416439, 0.009688287824743522],
        [0.3168637594191297, 0.11027608542619098, 0.5543078666062456, 0.01855228854843353],
        [0.04163620290872733, 0.04096739668332095, 0.039408962262072376, 0.8779874381458793],
        [0.024332762019173178, 0.8224530848950756, 0.07256575304288336, 0.08064840004286786],
        [0.03815378124246207, 0.06380212485362807, 0.862502416385161, 0.03554167751874892],
        [0.25, 0.25, 0.25, 0.25],
        [0.01956486399821184, 0.048046550681780674, 0.8322957138497722, 0.1000928714702353],
        [0.9569468698393323, 0.01522765557082897, 0.017742079630189957, 0.010083394959648726],
        [0.014045553172020414, 0.9603844908424684, 0.013895567902726474, 0.011674388082784712],
        [0.9152979305836279, 0.03361918744262919, 0.023088802520266054, 0.027994079453476813],
        [0.25, 0.25, 0.25, 0.25],
        [0.25, 0.25, 0.25, 0.25],
    ]
    return attack_vector, defense_vector