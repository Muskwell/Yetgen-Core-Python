from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


tarifler = [
    {
        "isim": "Baklava",
        "malzemeler": ["yufka", "ceviz", "tereyağı", "şeker", "su", "limon suyu"],
        "yapilis": "Yufkaları tereyağı ile yağlayarak üst üste koyun. Cevizleri serpip tekrar yufka ekleyin. Şeker ve suyu kaynatıp limon suyu ekleyin. Fırında pişirip şerbeti dökün."
    },
    {
        "isim": "Revani",
        "malzemeler": ["semolina", "yoğurt", "şeker", "yumurta", "kabartma tozu", "hindistancevizi"],
        "yapilis": "Yumurta ve şekeri çırpın, yoğurt ve kabartma tozunu ekleyin. Semolina ve hindistancevizini ekleyip karıştırın. Fırında pişirin, şerbetle buluşturun."
    },
    {
        "isim": "Sütlaç",
        "malzemeler": ["pirinç", "süt", "şeker", "vanilya", "tarçın"],
        "yapilis": "Sadece bir kez sudan geçirerek yıkadığınız pirinci tencereye alın ve 2 su bardağı sıcak suyu ekleyerek kısık ateşte pişirmeye başlayın.            Bu sırada ara ara nazikçe karıştırın.Pirinç, suyu çekip lapa hale gelince üzerine sütü ilave edin.Karıştırın ve süt kaynayana kadar ara ara karıştırmaya devam edin. Kaynadıktan sonra altını kısın, 8-10 dakika daha bu şekilde karıştırarak kısık ateşte pişirin.Ardından şekeri ekleyin, karıştırın. Tekrar kaynamasını bekleyin ve 4-5 dakika daha da kısık ateşte bu şekilde kaynatın. Nişastayı eklemek için bir kabın içerisine alın, 1 çay bardağı suyla karıştırın."
    },
    {
        "isim": "Künefe",
        "malzemeler": ["kadayıf", "tel kadayıf", "peynir", "tereyağı", "şeker", "su"],
        "yapilis": "Kadayıfı tereyağı ile yağlayıp tepsiye yayın. Peynir ekleyip üzerini kapatın. Şeker ve su ile şerbet hazırlayıp pişen künefeye dökün."
    },
    {
        "isim": "Çikolatalı Mousse",
        "malzemeler": ["bitter çikolata", "krema", "yumurta", "şeker", "vanilya"],
        "yapilis": "Çikolatanın yarısını eritin. Kremayı çırpın. Yumurta ve şekeri çırpın. Hepsini birleştirip kaselere dökün."
    },
    {
        "isim": "Tiramisu",
        "malzemeler": ["kedi dili", "kahve", "mascarpone peyniri", "şeker", " kakao"],
        "yapilis": "Kedidilini kahveye batırın. Mascarpone ve şekeri karıştırın. Kat kat dizip üzerine kakao serpin."
    },
    {
        "isim": "Pasta",
        "malzemeler": ["un", "şeker", "yumurta", "tereyağı", "vanilya", "süt"],
        "yapilis": "Malzemeleri çırpın. Karışımı kalıba döküp pişirin. Soğuduktan sonra dilediğiniz gibi süsleyin."
    },
    {
        "isim": "Zebra Kek",
        "malzemeler": ["un", "şeker", "yumurta", "süt", "kakao", "kabartma tozu"],
        "yapilis": "Malzemeleri karıştırın. Beyaz ve kakaolu hamuru sırayla kalıba dökün. Pişirip dilimleyin."
    },
    {
        "isim": "Panna Cotta",
        "malzemeler": ["krema", "şeker", "jelatin", "vanilya", "meyve sosu"],
        "yapilis": "Krema ve şekeri kaynatın, jelatini ekleyin. Kaselere döküp soğutun. Üzerine meyve sosu ekleyin."
    },
    {
        "isim": "Fırın Sütlaç",
        "malzemeler": ["pirinç", "süt", "şeker", "yumurta", "vanilya"],
        "yapilis": "Pirinci haşlayın, süte ekleyin. Şeker ve yumurtayı karıştırıp fırında pişirin."
    },
    {
        "isim": "Karamel Puding",
        "malzemeler": ["süt", "şeker", "yumurta", "vanilya", "karamel"],
        "yapilis": "Şekeri eritip karamel yapın. Diğer malzemeleri karıştırıp karamelin üzerine dökün. Fırında pişirin."
    },
    {
        "isim": "Şekerpare",
        "malzemeler": ["un", "şeker", "tereyağı", "yumurta", "badam"],
        "yapilis": "Malzemeleri yoğurup hamur yapın. Küçük parçalar oluşturup badem ile süsleyin. Şeker şerbeti ile buluşturun."
    },
    {
        "isim": "Aşure",
        "malzemeler": ["buğday", "nohut", "fasulye", "şeker", "ceviz", "kuru meyve"],
        "yapilis": "Buğdayı haşlayın, diğer malzemeleri ekleyin. Kaynatın ve kaselere döküp süsleyin."
    },
    {
        "isim": "Kozalak",
        "malzemeler": ["un", "şeker", "tereyağı", "yumurta", "hindistancevizi"],
        "yapilis": "Hamuru hazırlayıp şekil verin. Hindistancevizi ile kaplayıp fırında pişirin."
    },
    {
        "isim": "Dondurma",
        "malzemeler": ["süt", "şeker", "vanilya", "krema"],
        "yapilis": "Süt, şeker ve vanilyayı karıştırın. Krema ekleyip dondurma makinesinde dondurun."
    },
    {
        "isim": "Muzlu Puding",
        "malzemeler": ["süt", "şeker", "un", "muz"],
        "yapilis": "Süt ve şekeri kaynatın, un ekleyin. Muz dilimleri ile servis edin."
    },
    {
        "isim": "Kabak Tatlısı",
        "malzemeler": ["kabak", "şeker", "ceviz", "tarçın"],
        "yapilis": "Kabakları dilimleyin, şeker ile kaynatın. Ceviz ve tarçın ile süsleyin."
    },
    {
        "isim": "Peynir Tatlısı",
        "malzemeler": ["peynir", "un", "şeker", "yumurta"],
        "yapilis": "Malzemeleri yoğurup hamur haline getirin. Küçük parçalar oluşturup kızartın."
    },
    {
        "isim": "Çikolatalı Kek",
        "malzemeler": ["un", "şeker", "yumurta", "bitter çikolata"],
        "yapilis": "Tüm malzemeleri karıştırın. Fırında pişirin."
    },
    {
        "isim": "Elmalı Turta",
        "malzemeler": ["un", "şeker", "elma", "tarçın", "tereyağı"],
        "yapilis": "Hamuru açıp elma ve tarçın ile doldurun. Üzerini kapatıp fırında pişirin."
    },
    {
        "isim": "Sakızlı Muhallebi",
        "malzemeler": ["süt", "şeker", "nişasta", "sakız"],
        "yapilis": "Malzemeleri karıştırıp kaynatın. Kaselere döküp soğutun."
    },
    {
        "isim": "Tahinli Kumpir",
        "malzemeler": ["patates", "tahin", "şeker", "ceviz"],
        "yapilis": "Patatesleri haşlayın, tahin ve şeker ile karıştırın. Üzerine ceviz ekleyin."
    },
    {
        "isim": "Kavun Tatlısı",
        "malzemeler": ["kavun", "şeker", "limon"],
        "yapilis": "Kavunları dilimleyin, şeker ile karıştırıp bekletin. Limon suyu ile servis edin."
    },
    {
        "isim": "Çilekli Pasta",
        "malzemeler": ["kedi dili", "çilek", "krema", "şeker"],
        "yapilis": "Kedidilini çilek ve krema ile kat kat dizin. Üzerine çilek ekleyin."
    },
    {
        "isim": "Mercimek Çorbası",
        "malzemeler": ["kırmızı mercimek", "soğan", "carrot", "patates", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Soğanı ve havucu doğrayın. Zeytinyağında kavurun. Mercimek ve doğranmış patatesleri ekleyin. Üzerine su ekleyip kaynatın. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Tarator",
        "malzemeler": ["yoğurt", "salatalık", "sarımsak", "ceviz", "zeytinyağı", "tuz"],
        "yapilis": "Yoğurdu bir kaba alın. Rendelenmiş salatalık ve ezilmiş sarımsağı ekleyin. Doğranmış ceviz ve zeytinyağı ilave edin. Tuzla tatlandırın."
    },
    {
        "isim": "Ezogelin Çorbası",
        "malzemeler": ["kırmızı mercimek", "bulgur", "domates", "soğan", "nane", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Mercimek, bulgur, doğranmış domates ve baharatları ekleyin. Üzerine su ekleyip pişirin."
    },
    {
        "isim": "Kısır Çorbası",
        "malzemeler": ["bulgur", "domates", "salatalık", "soğan", "limon suyu", "zeytinyağı", "tuz"],
        "yapilis": "Bulguru sıcak suyla ıslatın. Doğranmış domates, salatalık ve soğanı ekleyin. Limon suyu, zeytinyağı ve tuz ile tatlandırın."
    },
    {
        "isim": "Tavuk Suyu Çorbası",
        "malzemeler": ["tavuk göğsü", "havuç", "patates", "soğan", "tuz", "karabiber", "su"],
        "yapilis": "Tavuk göğsünü ve doğranmış sebzeleri suyla birlikte kaynatın. Tuz ve karabiberle tatlandırın. Tavukları didikleyip çorbaya ekleyin."
    },
    {
        "isim": "Şehriye Çorbası",
        "malzemeler": ["şehriye", "soğan", "domates", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Doğranmış domatesleri ekleyin. Şehriyeyi ve suyu ilave edip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Kabak Çorbası",
        "malzemeler": ["kabak", "soğan", "patates", "yoğurt", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Soğanı ve patatesi doğrayıp zeytinyağında kavurun. Kabakları ekleyin ve su ilave edip pişirin. Karışımı blenderden geçirin ve yoğurtla tatlandırın."
    },
    {
        "isim": "Yoğurt Çorbası",
        "malzemeler": ["yoğurt", "un", "yumurta", "nane", "tuz", "su"],
        "yapilis": "Yoğurdu bir tencerede un ve yumurta ile çırpın. Üzerine su ekleyip kaynatın. Tuz ve nane ile tatlandırın."
    },
    {
        "isim": "Sebze Çorbası",
        "malzemeler": ["karışık sebzeler (havuç, patates, kabak)", "soğan", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Sebzeleri doğrayıp soğanla birlikte zeytinyağında kavurun. Üzerine su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Lentil Soup",
        "malzemeler": ["red lentils", "onion", "carrot", "potato", "salt", "black pepper", "olive oil"],
        "yapilis": "Chop onion and carrot. Sauté in olive oil. Add lentils and chopped potato. Add water and simmer. Season with salt and black pepper."
    },
    {
        "isim": "Cizre Çorbası",
        "malzemeler": ["kısır", "yoğurt", "nane", "sarımsak", "su", "tuz"],
        "yapilis": "Kısırı yoğurtla karıştırın. Nane ve sarımsağı ekleyin. Su ile karıştırıp kaynatın. Tuzla tatlandırın."
    },
    {
        "isim": "Bulgur Çorbası",
        "malzemeler": ["bulgur", "soğan", "domates", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Domatesleri ekleyin ve pişirin. Bulguru ekleyip su ekleyin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Mısırlı Çorba",
        "malzemeler": ["mısır", "soğan", "patates", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Patatesleri ekleyin ve mısırı ilave edin. Su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Domates Çorbası",
        "malzemeler": ["domates", "soğan", "zeytinyağı", "tuz", "karabiber", "su"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Doğranmış domatesleri ekleyin ve pişirin. Su ekleyip kaynatın. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Mercimek Yemeği",
        "malzemeler": ["kırmızı mercimek", "domates", "soğan", "tuz", "karabiber", "su"],
        "yapilis": "Soğanı doğrayıp kavurun. Mercimek ve doğranmış domatesleri ekleyin. Su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Kereviz Çorbası",
        "malzemeler": ["kereviz", "patates", "soğan", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Kereviz ve patatesi ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Pirinç Çorbası",
        "malzemeler": ["pirinç", "soğan", "tuz", "karabiber", "su"],
        "yapilis": "Soğanı doğrayıp kavurun. Pirinci ekleyin ve su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Tatlı Patates Çorbası",
        "malzemeler": ["tatlı patates", "soğan", "sarımsak", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Soğan ve sarımsağı doğrayıp zeytinyağında kavurun. Tatlı patatesleri ekleyin ve pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Pazı Çorbası",
        "malzemeler": ["pazı", "soğan", "patates", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Patates ve pazıyı ekleyin. Su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Kısır Çorbası",
        "malzemeler": ["kısır", "yoğurt", "nane", "sarımsak", "su", "tuz"],
        "yapilis": "Kısırı yoğurtla karıştırın. Nane ve sarımsağı ekleyin. Su ile karıştırıp kaynatın. Tuzla tatlandırın."
    },
    {
        "isim": "Makarna Çorbası",
        "malzemeler": ["makarna", "domates", "soğan", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Domatesleri ekleyin ve pişirin. Makarna ve suyu ekleyip kaynatın. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Cahide Çorbası",
        "malzemeler": ["mercimek", "patates", "soğan", "tuz", "karabiber", "su"],
        "yapilis": "Mercimek, patates ve soğanı doğrayıp suyla kaynatın. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Sebze Çorbası",
        "malzemeler": ["karışık sebzeler (havuç, patates, brokoli)", "soğan", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Sebzeleri doğrayıp soğanla birlikte zeytinyağında kavurun. Su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Mısır Çorbası",
        "malzemeler": ["mısır", "soğan", "patates", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Patates ve mısırı ekleyin. Su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Kabak Çorbası",
        "malzemeler": ["kabak", "soğan", "patates", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Soğan ve patatesi doğrayıp zeytinyağında kavurun. Kabakları ekleyin ve su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Mercimek Çorbası",
        "malzemeler": ["kırmızı mercimek", "soğan", "carrot", "patates", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Soğanı ve havucu doğrayın. Zeytinyağında kavurun. Mercimek ve doğranmış patatesleri ekleyin. Üzerine su ekleyip kaynatın. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Kısır Çorbası",
        "malzemeler": ["bulgur", "domates", "soğan", "limon suyu", "zeytinyağı", "tuz"],
        "yapilis": "Bulguru sıcak suyla ıslatın. Doğranmış domates ve soğanı ekleyin. Limon suyu, zeytinyağı ve tuz ile tatlandırın."
    },
    {
        "isim": "Şehriye Çorbası",
        "malzemeler": ["şehriye", "soğan", "domates", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Doğranmış domatesleri ekleyin. Şehriyeyi ve suyu ilave edip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Lentil Soup",
        "malzemeler": ["red lentils", "onion", "carrot", "potato", "salt", "black pepper", "olive oil"],
        "yapilis": "Chop onion and carrot. Sauté in olive oil. Add lentils and chopped potato. Add water and simmer. Season with salt and black pepper."
    },
    {
        "isim": "Kısır Çorbası",
        "malzemeler": ["bulgur", "domates", "salatalık", "soğan", "limon suyu", "zeytinyağı", "tuz"],
        "yapilis": "Bulguru sıcak suyla ıslatın. Doğranmış domates, salatalık ve soğanı ekleyin. Limon suyu, zeytinyağı ve tuz ile tatlandırın."
    },
    {
        "isim": "Bulgur Çorbası",
        "malzemeler": ["bulgur", "soğan", "domates", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Domatesleri ekleyin ve pişirin. Bulguru ekleyip su ekleyin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Mısırlı Çorba",
        "malzemeler": ["mısır", "soğan", "patates", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Patatesleri ekleyin ve mısırı ilave edin. Su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Domates Çorbası",
        "malzemeler": ["domates", "soğan", "zeytinyağı", "tuz", "karabiber", "su"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Doğranmış domatesleri ekleyin ve pişirin. Su ekleyip kaynatın. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Mercimek Çorbası",
        "malzemeler": ["kırmızı mercimek", "soğan", "carrot", "patates", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Soğanı ve havucu doğrayın. Zeytinyağında kavurun. Mercimek ve doğranmış patatesleri ekleyin. Üzerine su ekleyip kaynatın. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Kereviz Çorbası",
        "malzemeler": ["kereviz", "patates", "soğan", "tuz", "karabiber", "zeytinyağı"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Kereviz ve patatesi ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Pirinç Çorbası",
        "malzemeler": ["pirinç", "soğan", "tuz", "karabiber", "su"],
        "yapilis": "Soğanı doğrayıp kavurun. Pirinci ekleyin ve su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Tatlı Patates Çorbası",
        "malzemeler": ["tatlı patates", "soğan", "sarımsak", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Soğan ve sarımsağı doğrayıp zeytinyağında kavurun. Tatlı patatesleri ekleyin ve pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Pazı Çorbası",
        "malzemeler": ["pazı", "soğan", "patates", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Soğanı doğrayıp zeytinyağında kavurun. Patates ve pazıyı ekleyin. Su ekleyip pişirin. Tuz ve karabiberle tatlandırın."
    },
    {
        "isim": "Cacık",
        "malzemeler": ["yoğurt", "salatalık", "sarımsak", "zeytinyağı", "nane", "tuz"],
        "yapilis": "Yoğurdu bir kaba alın. Rendelenmiş salatalık, ezilmiş sarımsak ve tuzu ekleyin. Karıştırın. Üzerine zeytinyağı ve nane serpin."
    },
    {
        "isim": "Hummus",
        "malzemeler": ["nohut", "tahin", "zeytinyağı", "sarımsak", "limon suyu", "tuz"],
        "yapilis": "Nohutları haşlayın. Blenderda nohut, tahin, limon suyu, sarımsak ve tuzu karıştırın. Üzerine zeytinyağı gezdirin."
    },
    {
        "isim": "Acılı Ezme",
        "malzemeler": ["domates", "biber", "soğan", "zeytinyağı", "tuz", "nar ekşisi"],
        "yapilis": "Domates, biber ve soğanı ince doğrayın. Zeytinyağı, tuz ve nar ekşisi ile karıştırın."
    },
    {
        "isim": "Fava",
        "malzemeler": ["bakla", "soğan", "zeytinyağı", "limon suyu", "tuz", "karabiber"],
        "yapilis": "Baklaları haşlayın ve kabuklarını soyun. Soğanı kavurun. Baklaları ekleyin ve pişirin. Limon suyu, tuz ve karabiber ekleyin."
    },
    {
        "isim": "Pide",
        "malzemeler": ["un", "su", "maya", "zeytinyağı", "peynir", "sucuk"],
        "yapilis": "Un, su, maya ve zeytinyağını karıştırarak hamur yoğurun. Hamuru açıp üzerine peynir ve sucuk ekleyin. Fırında pişirin."
    },
    {
        "isim": "Zeytinyağlı Enginar",
        "malzemeler": ["enginar", "zeytinyağı", "limon suyu", "tuz", "şeker"],
        "yapilis": "Enginarları temizleyin. Zeytinyağı, limon suyu, tuz ve şeker ile pişirin."
    },
    {
        "isim": "Yoğurtlu Patlıcan",
        "malzemeler": ["patlıcan", "yoğurt", "sarımsak", "zeytinyağı", "tuz"],
        "yapilis": "Patlıcanları közleyin ve kabuklarını soyun. Yoğurt, ezilmiş sarımsak ve tuz ile karıştırın."
    },
    {
        "isim": "Sebzeli Kısır",
        "malzemeler": ["bulgur", "domates", "biber", "salatalık", "maydanoz", "nane"],
        "yapilis": "Bulguru sıcak suyla ıslatın. Doğranmış domates, biber, salatalık, maydanoz ve naneyi ekleyin. Karıştırın."
    },
    {
        "isim": "Patates Salatası",
        "malzemeler": ["patates", "soğan", "zeytinyağı", "tuz", "limon suyu"],
        "yapilis": "Patatesleri haşlayın ve doğrayın. Soğanı ince doğrayın. Zeytinyağı, tuz ve limon suyu ile karıştırın."
    },
    {
        "isim": "Börek",
        "malzemeler": ["yufka", "peynir", "yumurta", "zeytinyağı"],
        "yapilis": "Yufkaları kat kat açın. Peynir ve yumurta karışımını yufkaların arasına sürün. Fırında pişirin."
    },
    {
        "isim": "Muhammara",
        "malzemeler": ["kırmızı biber", "ceviz", "sarimsak", "zeytinyağı", "nar ekşisi"],
        "yapilis": "Közlenmiş biberleri ve cevizleri blenderda karıştırın. Sarımsak, zeytinyağı ve nar ekşisi ekleyin."
    },
    {
        "isim": "Tarator",
        "malzemeler": ["yoğurt", "salatalık", "ceviz", "sarımsak", "zeytinyağı", "tuz"],
        "yapilis": "Yoğurdu bir kaba alın. Rendelenmiş salatalık, ceviz, ezilmiş sarımsak ve tuzu ekleyin. Karıştırın."
    },
    {
        "isim": "Kısır",
        "malzemeler": ["bulgur", "domates", "maydanoz", "nane", "zeytinyağı", "limon"],
        "yapilis": "Bulguru sıcak suyla ıslatın. Doğranmış domates, maydanoz ve naneyi ekleyin. Zeytinyağı ve limon suyu ekleyerek karıştırın."
    },
    {
        "isim": "Zeytinyağlı Kısır",
        "malzemeler": ["bulgur", "domates", "soğan", "maydanoz", "nane", "zeytinyağı"],
        "yapilis": "Bulguru sıcak suyla ıslatın. Doğranmış domates, soğan, maydanoz ve naneyi ekleyin. Zeytinyağı ile karıştırın."
    },
    {
        "isim": "Patates Köftesi",
        "malzemeler": ["patates", "yumurta", "un", "tuz", "karabiber"],
        "yapilis": "Patatesleri haşlayın ve ezin. Yumurtayı ve unu ekleyin. Karışımı köfte şeklinde şekillendirip kızartın."
    },
    {
        "isim": "Cevizli Patlıcan",
        "malzemeler": ["patlıcan", "ceviz", "yoğurt", "sarımsak", "zeytinyağı"],
        "yapilis": "Patlıcanları közleyin ve kabuklarını soyun. Ceviz ve yoğurt ile karıştırın. Sarımsak ve zeytinyağı ekleyin."
    },
    {
        "isim": "İskenderun Usulü Humus",
        "malzemeler": ["nohut", "tahin", "zeytinyağı", "limon suyu", "sarımsak", "tuz"],
        "yapilis": "Nohutları haşlayın. Blenderda nohut, tahin, limon suyu, sarımsak ve tuzu karıştırın. Üzerine zeytinyağı gezdirin."
    },
    {
        "isim": "Roka Salatası",
        "malzemeler": ["roka", "limon suyu", "zeytinyağı", "tuz", "nar ekşisi"],
        "yapilis": "Rokayı yıkayın. Limon suyu, zeytinyağı, tuz ve nar ekşisi ile karıştırın."
    },
    {
        "isim": "Patates Cipsi",
        "malzemeler": ["patates", "zeytinyağı", "tuz"],
        "yapilis": "Patatesleri ince dilimleyin ve zeytinyağı ile fırında pişirin. Üzerine tuz serpin."
    },
    {
        "isim": "Cızlak",
        "malzemeler": ["yufka", "peynir", "yumurta", "zeytinyağı"],
        "yapilis": "Yufkayı dilimleyin ve peynir ile doldurun. Üzerine yumurta sürün ve tavada kızartın."
    },
    {
        "isim": "Lahmacun",
        "malzemeler": ["yufka", "kıyma", "domates", "biber", "soğan", "baharatlar"],
        "yapilis": "Yufkayı açın. Kıyma, doğranmış domates, biber ve soğanı karıştırarak yufkanın üzerine yayın. Fırında pişirin."
    },
    {
        "isim": "Peynirli Börek",
        "malzemeler": ["yufka", "peynir", "yumurta", "yoğurt", "zeytinyağı"],
        "yapilis": "Yufkaları kat kat açın. Peynir, yumurta ve yoğurt karışımını yufkaların arasına sürün. Fırında pişirin."
    },
    {
        "isim": "Havuçlu Kısır",
        "malzemeler": ["bulgur", "havuç", "maydanoz", "nane", "zeytinyağı", "limon"],
        "yapilis": "Bulguru sıcak suyla ıslatın. Rendelenmiş havuç, doğranmış maydanoz ve naneyi ekleyin. Zeytinyağı ve limon suyu ekleyerek karıştırın."
    },
    {
        "isim": "Yufkada Peynir",
        "malzemeler": ["yufka", "peynir", "maydanoz", "zeytinyağı"],
        "yapilis": "Yufkayı açın ve üzerine peynir ve doğranmış maydanoz ekleyin. Rulo yapıp kızartın."
    },
    {
        "isim": "Acılı Ezme",
        "malzemeler": ["domates", "biber", "soğan", "zeytinyağı", "tuz", "nar ekşisi"],
        "yapilis": "Domates, biber ve soğanı ince doğrayın. Zeytinyağı, tuz ve nar ekşisi ile karıştırın."
    },
    {
        "isim": "Fırın Patates",
        "malzemeler": ["patates", "zeytinyağı", "tuz", "baharatlar"],
        "yapilis": "Patatesleri doğrayın, zeytinyağı, tuz ve baharatlarla karıştırın. Fırında pişirin."
    },
    {
        "isim": "Zeytinyağlı Enginar",
        "malzemeler": ["enginar", "zeytinyağı", "limon suyu", "tuz", "şeker"],
        "yapilis": "Enginarları temizleyin. Zeytinyağı, limon suyu, tuz ve şeker ile pişirin."
    },
    {
        "isim": "Zeytinyağlı Kısır",
        "malzemeler": ["bulgur", "domates", "soğan", "maydanoz", "nane", "zeytinyağı"],
        "yapilis": "Bulguru sıcak suyla ıslatın. Doğranmış domates, soğan, maydanoz ve naneyi ekleyin. Zeytinyağı ile karıştırın."
    },
    {
        "isim": "Patates Kızartması",
        "malzemeler": ["patates", "zeytinyağı", "tuz"],
        "yapilis": "Patatesleri dilimleyin, zeytinyağı ile karıştırıp kızartın. Üzerine tuz serpin."
    },
    {
        "isim": "Peynirli Börek",
        "malzemeler": ["yufka", "peynir", "yumurta", "yoğurt", "zeytinyağı"],
        "yapilis": "Yufkaları kat kat açın. Peynir, yumurta ve yoğurt karışımını yufkaların arasına sürün. Fırında pişirin."
    },
    {
        "isim": "Köfte",
        "malzemeler": ["kıyma", "soğan", "ekmek içi", "yumurta", "baharatlar"],
        "yapilis": "Kıymayı, rendelenmiş soğanı, ekmek içini, yumurtayı ve baharatları karıştırıp yoğurun. Köfte şekli verip ızgarada pişirin."
    },
    {
        "isim": "İskender Kebabı",
        "malzemeler": ["kıyma", "yufka", "domates sosu", "yoğurt", "tereyağı"],
        "yapilis": "Kıymayı kebap şeklinde hazırlayın ve ızgarada pişirin. Yufkayı küçük parçalara kesin. Üzerine domates sosu ve yoğurt ekleyip tereyağı gezdirin."
    },
    {
        "isim": "Börek",
        "malzemeler": ["yufka", "peynir", "ıspanak", "yumurta", "zeytinyağı"],
        "yapilis": "Yufkaları kat kat dizin ve her kata peynir, ıspanak karışımı ekleyin. Üzerine yumurta ve zeytinyağı sürüp fırında pişirin."
    },
    {
        "isim": "Kuzu Tandır",
        "malzemeler": ["kuzu eti", "soğan", "patates", "havuç", "baharatlar"],
        "yapilis": "Kuzu etini baharatlarla ovun ve soğan, patates, havuç ekleyin. Fırında düşük sıcaklıkta uzun süre pişirin."
    },
    {
        "isim": "Karnıyarık",
        "malzemeler": ["patlıcan", "kıyma", "domates", "biber", "soğan", "baharatlar"],
        "yapilis": "Patlıcanları kızartın ve ortalarını açın. Kıymayı domates, biber, soğan ve baharatlarla kavurun. Patlıcanların içine doldurup fırında pişirin."
    },
    {
        "isim": "Fırın Tavuk",
        "malzemeler": ["tavuk", "patates", "havuç", "zeytinyağı", "baharatlar"],
        "yapilis": "Tavuğu baharatlarla ovun. Patates ve havuçları doğrayıp tavuğun yanına ekleyin. Fırında pişirin."
    },
    {
        "isim": "Dolma",
        "malzemeler": ["biber", "domates", "pirinç", "kıyma", "baharatlar"],
        "yapilis": "Biberleri ve domatesleri oyup iç harcını hazırlayın. Pirinç, kıyma ve baharatları karıştırıp dolmaların içine doldurun. Tencerede pişirin."
    },
    {
        "isim": "Sulu Köfte",
        "malzemeler": ["köfte", "domates", "patates", "havuç", "soğan", "baharatlar"],
        "yapilis": "Köfteleri hazırlayıp kızartın. Tencerede soğanı kavurun, doğranmış domates, patates ve havuç ekleyip köfteleri ilave edin. Su ve baharatlarla pişirin."
    },
    {
        "isim": "Biftek",
        "malzemeler": ["biftek", "zeytinyağı", "tuz", "karabiber"],
        "yapilis": "Bifteği zeytinyağı, tuz ve karabiberle ovun. Izgarada ya da tavada pişirin."
    },
    {
        "isim": "Kuzu Pirzola",
        "malzemeler": ["kuzu pirzola", "zeytinyağı", "soğan", "patates", "baharatlar"],
        "yapilis": "Pirzolaları zeytinyağı ve baharatlarla ovun. Soğan ve patatesle birlikte fırında pişirin."
    },
    {
        "isim": "Fırın Mantarı",
        "malzemeler": ["mantar", "peynir", "sarımsak", "zeytinyağı"],
        "yapilis": "Mantarları temizleyip zeytinyağı ve doğranmış sarımsak ile karıştırın. Peynir serpip fırında pişirin."
    },
    {
        "isim": "Sebze Kızartması",
        "malzemeler": ["patates", "kabak", "patlıcan", "zeytinyağı", "baharatlar"],
        "yapilis": "Sebzeleri doğrayıp zeytinyağı ve baharatlarla karıştırın. Fırında ya da tavada kızartın."
    },
    {
        "isim": "Şakşuka",
        "malzemeler": ["patlıcan", "domates", "biber", "soğan", "sarımsak", "baharatlar"],
        "yapilis": "Patlıcanları kızartın. Soğanı ve biberi kavurun, domates ve baharatları ekleyin. Patlıcanları ekleyip pişirin."
    },
    {
        "isim": "Mücver",
        "malzemeler": ["kabak", "yumurta", "un", "peynir", "maydanoz", "baharatlar"],
        "yapilis": "Kabaka rendelenmiş yumurta, un, peynir, maydanoz ve baharatları ekleyip karıştırın. Kızgın yağda kızartın."
    },
    {
        "isim": "Kuzu Tandır",
        "malzemeler": ["kuzu eti", "soğan", "patates", "havuç", "baharatlar"],
        "yapilis": "Kuzu etini baharatlarla ovun ve soğan, patates, havuç ekleyin. Fırında düşük sıcaklıkta uzun süre pişirin."
    },
    {
        "isim": "Yaprak Sarma",
        "malzemeler": ["üzüm yaprağı", "pirinç", "kıyma", "soğan", "baharatlar"],
        "yapilis": "Pirinci, kıymayı ve baharatları karıştırın. Üzüm yapraklarına sarıp tencerede pişirin."
    },
    {
        "isim": "Patates Yemeği",
        "malzemeler": ["patates", "soğan", "domates", "biber", "zeytinyağı"],
        "yapilis": "Soğanı zeytinyağında kavurun, doğranmış biber ve domates ekleyin. Patatesleri ekleyip pişirin."
    },
    {
        "isim": "Kumpir",
        "malzemeler": ["patates", "peynir", "zeytinyağı", "mısır", "salam", "zeytin"],
        "yapilis": "Patatesleri fırında pişirin. İçini ezip peynir, zeytinyağı, mısır, salam ve zeytin ekleyin."
    },
    {
        "isim": "Türlü",
        "malzemeler": ["patates", "kabak", "biber", "domates", "soğan", "baharatlar"],
        "yapilis": "Sebzeleri doğrayıp tencerede kavurun. Baharatlar ekleyip pişirin."
    },
    {
        "isim": "Fırında Tavuk",
        "malzemeler": ["tavuk", "patates", "havuç", "zeytinyağı", "baharatlar"],
        "yapilis": "Tavuğu baharatlarla ovun. Patates ve havuçları doğrayıp tavuğun yanına ekleyin. Fırında pişirin."
    },
    {
        "isim": "Fırın Köfte",
        "malzemeler": ["kıyma", "soğan", "ekmek içi", "yumurta", "baharatlar"],
        "yapilis": "Kıymayı, rendelenmiş soğanı, ekmek içini, yumurtayı ve baharatları karıştırıp yoğurun. Fırında pişirin."
    },
    {
        "isim": "Et Sote",
        "malzemeler": ["kuzu eti", "soğan", "biber", "domates", "baharatlar"],
        "yapilis": "Kuzu etini doğrayıp kavurun. Soğan, biber ve domates ekleyip pişirin. Baharatlarla tatlandırın."
    },
    {
        "isim": "Sebzeli Kısır",
        "malzemeler": ["bulgur", "domates", "salatalık", "maydanoz", "nane", "zeytinyağı", "limon"],
        "yapilis": "Bulguru sıcak suyla ıslatın. Doğranmış domates, salatalık, maydanoz ve naneyi ekleyin. Zeytinyağı ve limon suyu ekleyin."
    },
    {
        "isim": "Kuzu Güveç",
        "malzemeler": ["kuzu eti", "patates", "havuç", "soğan", "domates", "baharatlar"],
        "yapilis": "Kuzu etini doğrayıp sebzelerle birlikte güveçte pişirin. Baharatlarla tatlandırın."
    },
    {
        "isim": "Kumpir",
        "malzemeler": ["patates", "peynir", "zeytinyağı", "mısır", "salam", "zeytin"],
        "yapilis": "Patatesleri fırında pişirin. İçini ezip peynir, zeytinyağı, mısır, salam ve zeytin ekleyin."
    },
    {
        "isim": "Fırında Kuzu",
        "malzemeler": ["kuzu eti", "patates", "havuç", "soğan", "baharatlar"],
        "yapilis": "Kuzu etini baharatlarla ovun. Patates, havuç ve soğan ile birlikte fırında pişirin."
    },
    {
        "isim": "Börek",
        "malzemeler": ["yufka", "peynir", "ıspanak", "yumurta", "zeytinyağı"],
        "yapilis": "Yufkaları kat kat dizin ve her kata peynir, ıspanak karışımı ekleyin. Üzerine yumurta ve zeytinyağı sürüp fırında pişirin."
    },
    {
        "isim": "Omlet",
        "malzemeler": ["yumurta", "süt", "tuz", "karabiber", "tereyağı"],
        "yapilis": "Yumurta ve sütü çırpın. Tuz ve karabiber ekleyin. Tereyağını tavada eritin ve karışımı dökün. Pişene kadar karıştırın."
    },
    {
        "isim": "Menemen",
        "malzemeler": ["yumurta", "domates", "biber", "tuz", "zeytinyağı"],
        "yapilis": "Zeytinyağını tavada ısıtın. Doğranmış biberleri ekleyin ve kavurun. Doğranmış domatesleri ekleyin ve pişirin. Yumurtaları kırın ve karıştırarak pişirin."
    },
    {
        "isim": "Makarna",
        "malzemeler": ["makarna", "zeytinyağı", "tuz", "su", "domates"],
        "yapilis": "Makarnayı tuzlu suda haşlayın. Zeytinyağını tavada ısıtın, doğranmış domatesleri ekleyin ve pişirin. Haşlanmış makarnayı ekleyin ve karıştırın."
    },
    {
        "isim": "Salata",
        "malzemeler": ["marul", "domates", "salatalık", "zeytinyağı", "limon"],
        "yapilis": "Marul, domates ve salatalığı doğrayın. Zeytinyağı ve limon suyu ekleyerek karıştırın."
    },
    {
        "isim": "Pilav",
        "malzemeler": ["pirinç", "su", "tereyağı", "tuz"],
        "yapilis": "Pirinci yıkayın. Tencereye su ve tuz ekleyin. Pirinci ekleyin ve pişirin. Piştikten sonra tereyağı ekleyin ve karıştırın."
    },
    {
        "isim": "Patates Kızartması",
        "malzemeler": ["patates", "tuz", "yağ"],
        "yapilis": "Patatesleri doğrayın. Yağı kızdırın ve patatesleri kızartın. Tuz ekleyin ve servis edin."
    },
    {
        "isim": "Pancake",
        "malzemeler": ["un", "süt", "yumurta", "şeker", "kabartma tozu"],
        "yapilis": "Un, süt, yumurta, şeker ve kabartma tozunu karıştırın. Tavada pişirin ve servis edin."
    },
    {
        "isim": "Fırın Tavuk",
        "malzemeler": ["tavuk", "zeytinyağı", "tuz", "karabiber", "baharat"],
        "yapilis": "Tavuğu zeytinyağı, tuz, karabiber ve baharatla ovun. Fırında pişirin."
    },
    {
        "isim": "Bulgur Pilavı",
        "malzemeler": ["bulgur", "domates", "soğan", "su", "tuz"],
        "yapilis": "Soğanı kavurun, domatesleri ekleyin. Bulguru ekleyin, su ve tuz ekleyip pişirin."
    },
    {
        "isim": "Sıcak Sandviç",
        "malzemeler": ["ekmek", "sucuk", "kaşar peyniri", "tereyağı"],
        "yapilis": "Ekmeklerin arasına sucuk ve kaşar peynirini koyun. Tereyağında kızartın."
    },
]


class Tarif:
    def __init__(self, isim, malzemeler, yapilis):
        self.isim = isim
        self.malzemeler = malzemeler
        self.yapilis = yapilis

    def uygun_mu(self, verilen_malzemeler):
        return set(verilen_malzemeler).issubset(self.malzemeler)


def tarif_bul(malzemeler):
    malzemeler_set = set(malzemeler)
    uygun_tarifler = []
    
    
    for tarif in tarifler:
        if malzemeler_set.issubset(set(tarif["malzemeler"])):
            uygun_tarifler.append(tarif)
    
    
    for tarif in yeni_tarifler:
        if tarif.uygun_mu(malzemeler_set):
            uygun_tarifler.append({
                "isim": tarif.isim,
                "malzemeler": tarif.malzemeler,
                "yapilis": tarif.yapilis
            })
    
    return uygun_tarifler


yeni_tarifler = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        malzemeler = [m.strip().lower() for m in request.form['malzemeler'].split(",")]
        if len(malzemeler) == 3:
            uygun_tarifler = tarif_bul(malzemeler)
            return render_template('tarifler.html', tarifler=uygun_tarifler)
        else:
            return render_template('index.html', mesaj="Lütfen tam olarak 3 malzeme girin.")
    return render_template('index.html')


@app.route('/tarif/<tarif_adi>')
def tarif(tarif_adi):
    yapilis = None
    
    
    for tarif in tarifler:
        if tarif["isim"].lower() == tarif_adi.lower():
            yapilis = tarif["yapilis"]
            break
    
    
    if not yapilis:
        for tarif in yeni_tarifler:
            if tarif.isim.lower() == tarif_adi.lower():
                yapilis = tarif.yapilis
                break

    if yapilis:
        return render_template('tarif_detay.html', tarif_adi=tarif_adi, yapilis=yapilis)
    return "Tarif bulunamadı."


@app.route('/tarif-ekle', methods=['GET', 'POST'])
def tarif_ekle():
    if request.method == 'POST':
        isim = request.form.get('isim', '').strip()
        malzemeler = [m.strip().lower() for m in request.form.get('malzemeler', '').split(",")]
        yapilis = request.form.get('yapilis', '').strip()


        hata_mesajlari = []
        if not isim:
            hata_mesajlari.append("Tarif ismi boş olamaz.")
        if not malzemeler or malzemeler == ['']:
            hata_mesajlari.append("Malzemeler boş olamaz.")
        if not yapilis:
            hata_mesajlari.append("Tarifin yapılışı boş olamaz.")

        if hata_mesajlari:
            return render_template('tarif_ekle.html', hata_mesajlari=hata_mesajlari)
        
        yeni_tarif = Tarif(isim, malzemeler, yapilis)
        yeni_tarifler.append(yeni_tarif)
        return redirect(url_for('index'))
    
    return render_template('tarif_ekle.html')

if __name__ == '__main__':
    app.run(debug=True)