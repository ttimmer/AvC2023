import re
def map_solution(seeds,map):
    mapped_values = seeds
    indexesAlreadyDone = []
    for entry in map:
        numbers = re.findall(r'\d+', entry);
        seedindex=0
        for seed in seeds:
           # print(f"Seed is {seed} and range is {numbers[1]} -{int(numbers[1])+int(numbers[2])} ")
            if int(seed) >= int(numbers[1]) and int(seed) <= int(numbers[1])+int(numbers[2]) and not (seedindex in indexesAlreadyDone):
                mapped_values[seedindex] = int(seed) + int(numbers[0])-int(numbers[1])
                indexesAlreadyDone.append(seedindex)
            seedindex+=1
    return mapped_values
def map_solution_2(seed_ranges,map):
    mapped_seed_ranges = []
    print(seed_ranges)
    for seed_range in seed_ranges:
        entry = find_range(seed_range,map)
        mapped_seed_ranges.extend(entry)
    print(f"End of mapping total {mapped_seed_ranges}")
    return mapped_seed_ranges

def find_range(seed_range,map):
    mapped_seed_ranges = []
    print(f"Seed_range from ranges {seed_range}")
    seed_range_start = seed_range[0]
    seed_range_end = seed_range[1]
    xFoundEntry = False
    for entry in map:
        numbers = re.findall(r'\d+', entry);
        print(f"Should find {seed_range_start} to {seed_range_end} between {int(numbers[1])} and {int(numbers[1])+ int(numbers[2])} ")
        if seed_range_start >= int(numbers[1]) and seed_range_end <= int(numbers[1])+int(numbers[2]): # fully in map
            new_seed_start = int(seed_range_start) + int(numbers[0])-int(numbers[1])
            new_seed_end = int(seed_range_end) + int(numbers[0])-int(numbers[1])
            print(f"found completely")
            mapped_seed_ranges.append([new_seed_start,new_seed_end])
            print(f"End of mapping this range {mapped_seed_ranges}")
            return mapped_seed_ranges
        elif seed_range_start >= int(numbers[1]) and seed_range_start <=int(numbers[1])+int(numbers[2]): # start lies between map
            print(f"found partly {seed_range_start} to {int(numbers[1])+int(numbers[2])} ")
            new_seed_start = int(seed_range_start) + int(numbers[0])-int(numbers[1])
            new_seed_end = int(numbers[1])+int(numbers[2]) + int(numbers[0])-int(numbers[1])
            mapped_seed_ranges.append([new_seed_start,new_seed_end])
            new_seed_start = int(numbers[1])+int(numbers[2]) + 1
            new_seed_end = seed_range_end
            mapped_seed_ranges.extend(find_range([new_seed_start,new_seed_end],map))
            print(f"End of mapping this range {mapped_seed_ranges}")
            return mapped_seed_ranges
        elif seed_range_end >= int(numbers[1]) and seed_range_end <=int(numbers[1])+int(numbers[2]): # end lies between map
            print(f"found partly {int(numbers[1])} to {int(numbers[1])+int(numbers[2])} ")
            new_seed_start = int(seed_range_start)
            new_seed_end = int(numbers[1])-1
            mapped_seed_ranges.extend(find_range([new_seed_start,new_seed_end],map))
            new_seed_start = int(numbers[1])+ int(numbers[0])-int(numbers[1])
            new_seed_end = seed_range_end+ int(numbers[0])-int(numbers[1])
            mapped_seed_ranges.append([new_seed_start,new_seed_end])
            print(f"End of mapping this range {mapped_seed_ranges}")
            return mapped_seed_ranges
    if not xFoundEntry:
        mapped_seed_ranges.append([seed_range_start,seed_range_end])
        print(f'Not found so keeping as is {mapped_seed_ranges}')
    print(f"End of mapping this range {mapped_seed_ranges}")
    return mapped_seed_ranges

def perform_solution(input):
    input_lines = input.split("\n")
    seeds = re.findall(r'\d+', input_lines[1]);


    index = 0
    xseed2soil = False
    aseed2soil = []
    xsoil2fertilizer = False
    asoil2fertilizer = []
    xfertilizer2water = False
    afertilizer2waterr = []
    xwater2light = False
    awater2light = []
    xLight2Temp = False
    aLight2Temp = []
    xtemp2humid = False
    atemp2humid = []
    xHumidity2Loc = False
    aHumidity2Loc = []
    for line in input_lines:
        if line == '':
            xseed2soil = False
            xsoil2fertilizer = False
            xfertilizer2water = False
            xwater2light = False
            xLight2Temp = False
            xtemp2humid = False
            xHumidity2Loc = False

        if xseed2soil:
            aseed2soil.append(line)
        elif xsoil2fertilizer:
            asoil2fertilizer.append(line)
        elif xfertilizer2water:
            afertilizer2waterr.append(line)
        elif xwater2light:
            awater2light.append(line)
        elif xLight2Temp:
            aLight2Temp.append(line)
        elif xtemp2humid:
            atemp2humid.append(line)
        elif xHumidity2Loc:
            aHumidity2Loc.append(line)

        if line == 'seed-to-soil map:':
            xseed2soil = True
        elif line == 'soil-to-fertilizer map:':
            xsoil2fertilizer = True
        elif line == 'fertilizer-to-water map:':
            xfertilizer2water = True
        elif line == 'water-to-light map:':
            xwater2light = True
        elif line == 'light-to-temperature map:':
            xLight2Temp = True
        elif line == 'temperature-to-humidity map:':
            xtemp2humid = True
        elif line == 'humidity-to-location map:':
            xHumidity2Loc = True

        index += 1
    asoil= map_solution(seeds,aseed2soil)
    afertilizer= map_solution(asoil,asoil2fertilizer)
    awater= map_solution(afertilizer,afertilizer2waterr)
    alight= map_solution(awater,awater2light)
    atemp= map_solution(alight,aLight2Temp)
    ahumid= map_solution(atemp,atemp2humid)
    alocation= map_solution(ahumid,aHumidity2Loc)
    abiggestlocation = 999999999999999999999999999999999999999999999999999999999999999999999999999999999
    for location in alocation:
        if int(location)<abiggestlocation:
            abiggestlocation=int(location)
    return(abiggestlocation)

def perform_solution2(input):
    input_lines = input.split("\n")
    seeds = re.findall(r'\d+', input_lines[1]);
    new_seeds = []
    for i in range(int(len(seeds)/2)):
        new_seeds.append([int(seeds[2*i]), int(seeds[2*i])+int(seeds[2*i+1])])
    seeds = new_seeds
    index = 0
    xseed2soil = False
    aseed2soil = []
    xsoil2fertilizer = False
    asoil2fertilizer = []
    xfertilizer2water = False
    afertilizer2waterr = []
    xwater2light = False
    awater2light = []
    xLight2Temp = False
    aLight2Temp = []
    xtemp2humid = False
    atemp2humid = []
    xHumidity2Loc = False
    aHumidity2Loc = []
    for line in input_lines:
        if line == '':
            xseed2soil = False
            xsoil2fertilizer = False
            xfertilizer2water = False
            xwater2light = False
            xLight2Temp = False
            xtemp2humid = False
            xHumidity2Loc = False

        if xseed2soil:
            aseed2soil.append(line)
        elif xsoil2fertilizer:
            asoil2fertilizer.append(line)
        elif xfertilizer2water:
            afertilizer2waterr.append(line)
        elif xwater2light:
            awater2light.append(line)
        elif xLight2Temp:
            aLight2Temp.append(line)
        elif xtemp2humid:
            atemp2humid.append(line)
        elif xHumidity2Loc:
            aHumidity2Loc.append(line)

        if line == 'seed-to-soil map:':
            xseed2soil = True
        elif line == 'soil-to-fertilizer map:':
            xsoil2fertilizer = True
        elif line == 'fertilizer-to-water map:':
            xfertilizer2water = True
        elif line == 'water-to-light map:':
            xwater2light = True
        elif line == 'light-to-temperature map:':
            xLight2Temp = True
        elif line == 'temperature-to-humidity map:':
            xtemp2humid = True
        elif line == 'humidity-to-location map:':
            xHumidity2Loc = True

        index += 1

    asoil= map_solution_2(seeds,aseed2soil)
    print(f"asoil {asoil}")
    afertilizer= map_solution_2(asoil,asoil2fertilizer)
    print(f"afertilizer {afertilizer}")
    awater= map_solution_2(afertilizer,afertilizer2waterr)
    print(f"awater {awater}")
    alight= map_solution_2(awater,awater2light)
    print(f"alight {alight}")
    atemp= map_solution_2(alight,aLight2Temp)
    print(f"atemp {atemp}")
    ahumid= map_solution_2(atemp,atemp2humid)
    print(f"ahumid {ahumid}")
    alocation= map_solution_2(ahumid,aHumidity2Loc)

    print(f"This is the locationlist {alocation}")

    abiggestlocation = 999999999999999999999999999999999999999999999999999999999999999999999999999999999
    for location in alocation:
        lowestlocation= int(location[0])
        if lowestlocation<abiggestlocation:
            abiggestlocation=lowestlocation
    return(abiggestlocation)






if __name__ == '__main__':
    input_test = """seeds:
79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    solution_test1 = 35
    if (solution_test1== perform_solution(input_test)):
        print("Test 1 works")
    else:
        print(perform_solution(input_test))

    input_actual ="""seeds:
4188359137 37519573 3736161691 172346126 2590035450 66446591 209124047 106578880 1404892542 30069991 3014689843 117426545 2169439765 226325492 1511958436 177344330 1822605035 51025110 382778843 823998526

seed-to-soil map:
1014943420 3864598346 36796924
3481858860 1134944893 176050938
1463359964 377309295 172917932
1909673912 2511534001 114785858
3472030089 1310995831 9828771
188280292 3055921442 55776498
352078282 1410745074 662865138
1436499332 3759669547 26860632
281816159 550227227 70262123
2940933503 180112079 197197216
3314718477 977633281 157311612
3269652387 3354932755 45066090
3138688421 4164003330 130963966
3689427547 3407181792 70304018
2673867052 3901395270 21291616
3881132258 2371714487 139819514
180112079 3751501334 8168213
2471524173 3399998845 7182947
244056790 3826838977 37759369
2330362750 620489350 141161423
1730119344 3786530179 40308798
1770428142 4040990485 122455143
1892883285 4024199858 16790627
3657909798 2340196738 31517749
1365072738 2268770144 71426594
1636277896 3930358410 93841448
1173574466 2626319859 183826748
3871069976 3233532062 10062282
3138130719 4163445628 557702
3759731565 3243594344 111338411
1357401214 3922686886 7671524
2478707120 2073610212 195159932
2695158668 2810146607 245774835
1051740344 3111697940 121834122
2024459770 761650773 215982508
2240442278 1320824602 89920472
4020951772 3477485810 274015524

soil-to-fertilizer map:
3211509025 2411974869 518394
3778955089 2412493263 120143427
1387254723 3589309701 265617279
3899098516 3906385182 120055953
1714049028 3209939839 261248850
3687768172 2393589437 18385432
554325135 488411873 327969675
2579624415 1520719313 60457941
4019154469 1244906486 275812827
65913262 0 488411873
1244906486 2362023384 31566053
2251369843 4026441135 268526161
0 826989738 65913262
3737515035 2233559302 41440054
1975297878 2563998121 276071965
3606812793 2152603923 80955379
3706153604 2532636690 31361431
1327930741 2336176382 25847002
3262441387 2840070086 276664362
1353777743 3176462859 33476980
1007455475 962102883 213088648
3212027419 3538895733 50413968
2519896004 3116734448 59728411
938255592 892903000 69199883
3539105749 3471188689 67707044
2640082356 1581177254 571426669
927647402 816381548 10608190
882294810 1175191531 45352592
1652872002 2274999356 61177026
1276472539 3854926980 51458202

fertilizer-to-water map:
3919934952 4034286493 116558226
3104838986 886102234 15848522
151486725 1109841455 112301087
38656834 2035810690 62773281
1106567462 3087125934 135164894
1010741746 2114463748 17027276
1428501666 0 69192244
1241732356 699332924 186769310
728534624 1829633882 45432965
465497393 318840419 263037231
263787812 69192244 201709581
1750247416 2131491024 226195640
3103410010 1396336613 1428976
1541007057 2541565636 209240359
2557596892 1222142542 146760701
3810606692 4150844719 109328260
1497693910 2098583971 15879777
2027240691 1925694260 110116430
3120687508 1664856712 30800728
2919531038 2357686664 183878972
2271333563 2800862605 286263329
0 660676090 38656834
121820432 2771196312 29666293
773967589 1428082555 236774157
2137357121 1695657440 133976442
2704357593 270901825 47938594
2782613153 952748391 136917885
4200808114 3619712494 94159182
1513573687 1368903243 27433370
3151488236 1875066847 50627413
4036493178 4260172979 34794317
1027769022 581877650 78798440
3202115649 1089666276 20175179
4071287495 3713871676 33593925
1976443056 901950756 50797635
2752296187 1397765589 30316966
101430115 2750805995 20390317
4104881420 3523785800 95926694
3523785800 3747465601 286820892

water-to-light map:
3408155249 2527370950 73535457
1697763259 1358503385 195569028
4146691798 4150439777 2978835
1667104621 3141702962 30658638
3109198454 2600906407 225322957
2896907826 3481425874 212290628
3568598531 1256359145 28510402
1021594560 3172361600 54292616
2709047387 0 23043868
634713149 1912815102 64867237
2732091255 3693716502 115595269
4005143114 4153418612 141548684
1341220299 1554072413 325884322
3514549073 2826229364 54049458
1113545862 2299696513 227674437
3481690706 1879956735 32858367
379941491 3226654216 254771658
4149670633 4005143114 145296663
699580386 1977682339 322014174
2847686524 2880278822 49221302
1075887176 23043868 37658686
3334521411 1284869547 73633838
3597108933 2929500124 212202838
1893332287 440644045 815715100
0 60702554 379941491

light-to-temperature map:
3239555722 2588818955 376881377
413170934 1615450109 438931580
1386539780 3880234113 95792562
3901352290 2965700332 122376625
2415511159 396206595 236868242
396206595 3092807515 16964339
2652379401 633074837 587176321
1998109231 1220251158 178061188
2176170419 3109771854 239340740
852102514 2054381689 534437266
1806003521 3349112594 192105710
1487062900 3976026675 318940621
1482332342 3088076957 4730558
3616437099 3687776838 138356657
3754793756 3541218304 146558534
4077829533 1398312346 217137763
4023728915 3826133495 54100618

temperature-to-humidity map:
2477444013 1065021126 6182773
845330217 1308005650 445611689
1290941906 3378900568 76961272
2975821403 1792935684 125881029
2161173272 2394771508 172817491
2483626786 3710234886 492194617
3447920062 2383111679 11659829
4033768577 1918816713 94002198
3319210784 3455861840 27565379
1373852246 1071203899 92358857
3101702432 845330217 174648768
2026258159 2567588999 134915113
1799450492 3483427219 226807667
3552117684 3041692569 337207999
3889325683 1163562756 144442894
3346776163 2047917336 101143899
3459579891 4202429503 92537793
0 348737431 60744241
1367903178 2829658946 5949068
1466211103 2702504112 127154834
1764704299 2835608014 34746193
60744241 322208375 20457270
1593365937 2870354207 171338362
81201511 342665645 6071786
4255648951 1753617339 39318345
2442345588 2012818911 35098425
2333990763 2231897270 108354825
87273297 0 322208375
4210606810 1019978985 45042141
3276351200 2340252095 42859584
4127770775 2149061235 82836035

humidity-to-location map:
4164635022 1854717524 130332274
1293632444 529805154 119897086
2886189584 4227662016 67305280
2977935483 447338344 82466810
1796689277 771172820 2500486
3592167651 2376391709 149158288
85140393 196642481 8447522
1799189763 1985049798 97611367
93587915 82281848 114360633
1191989560 4020597507 76356570
2953494864 3996156888 24440619
2292169251 649702240 113196341
3741325939 3311723608 237145571
3978471510 3948521384 47635504
2457376544 762898581 6077326
1413529530 768975907 2196913
1268346130 3923235070 25286314
4064092089 3749326886 100542933
2463453870 3849869819 73365251
2858545 0 82281848
4026107014 4166840403 37985075
3060402293 223340676 11429685
0 205090003 2858545
3071831978 1031969734 125782276
895745297 2082661165 83676280
513318799 1318499280 382426498
2536819121 3548869179 86842399
2405365592 1157752010 52010952
2086131564 3105685921 206037687
1972516256 3635711578 113615308
3197614254 2921186788 184499133
3382113387 2166337445 210054264
383000830 933333460 37595105
2777453266 1209762962 108736318
443432473 4096954077 69886326
1461500584 2540223954 335188693
1415726443 2875412647 45774141
420595935 4204825478 22836538
979421577 234770361 212567983
223340676 773673306 159660154
1911475087 970928565 61041169
1896801130 2525549997 14673957
2623661520 1700925778 153791746"""


    print(perform_solution(input_actual))
    solution_test2=46
    if (solution_test2== (perform_solution2(input_test))):
        print("Test 2 works")
    else:
        pass;#print(perform_solution2(input_test))

    print(perform_solution2(input_actual))
