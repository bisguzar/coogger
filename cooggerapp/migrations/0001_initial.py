# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-08 01:28
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('male', 'erkek'), ('female', 'kadın')], max_length=6, verbose_name='cinsiyet')),
                ('county', models.CharField(choices=[('adana', 'adana'), ('adyaman', 'adıyaman'), ('afyon', 'afyon'), ('agr', 'ağrı'), ('amasya', 'amasya'), ('ankara', 'ankara'), ('antalya', 'antalya'), ('artvin', 'artvin'), ('aydn', 'aydın'), ('balkesir', 'balıkesir'), ('bilecik', 'bilecik'), ('bingol', 'bingöl'), ('bitlis', 'bitlis'), ('bolu', 'bolu'), ('burdur', 'burdur'), ('bursa', 'bursa'), ('canakkale', 'çanakkale'), ('cankr', 'çankırı'), ('corum', 'çorum'), ('denizli', 'denizli'), ('diyarbakr', 'diyarbakır'), ('edirne', 'edirne'), ('elazg', 'elazığ'), ('erzincan', 'erzincan'), ('erzurum', 'erzurum'), ('eskisehir', 'eskişehir'), ('gaziantep', 'gaziantep'), ('giresun', 'giresun'), ('gumushane', 'gümüşhane'), ('hakkari', 'hakkari'), ('hatay', 'hatay'), ('sparta', 'ısparta'), ('mersin', 'mersin'), ('istanbul', 'istanbul'), ('izmir', 'izmir'), ('kars', 'kars'), ('kastamonu', 'kastamonu'), ('kayseri', 'kayseri'), ('krklareli', 'Kırklareli'), ('krsehir', 'kırşehir'), ('kocaeli', 'kocaeli'), ('konya', 'konya'), ('kutahya', 'kütahya'), ('malatya', 'malatya'), ('manisa', 'manisa'), ('kahramanmaras', 'kahramanmaraş'), ('mardin', 'mardin'), ('mugla', 'muğla'), ('mus', 'muş'), ('nevsehir', 'nevşehir'), ('nigde', 'niğde'), ('ordu', 'ordu'), ('rize', 'rize'), ('sakarya', 'sakarya'), ('samsun', 'samsun'), ('siirt', 'siirt'), ('sinop', 'sinop'), ('sivas', 'sivas'), ('tekirdag', 'tekirdağ'), ('tokat', 'tokat'), ('trabzon', 'trabzon'), ('tunceli', 'tunceli'), ('sanlurfa', 'şanlıurfa'), ('usak', 'uşak'), ('van', 'van'), ('yozgat', 'yozgat'), ('zonguldak', 'zonguldak'), ('aksaray', 'aksaray'), ('bayburt', 'bayburt'), ('karaman', 'karaman'), ('krkkale', 'kırıkkale'), ('batman', 'batman'), ('srnak', 'şırnak'), ('bartn', 'bartın'), ('ardahan', 'ardahan'), ('gdr', 'ığdır'), ('yalova', 'yalova'), ('karabuk', 'karabuk'), ('kilis', 'kilis'), ('osmaniye', 'osmaniye'), ('duzce', 'düzce')], max_length=50, verbose_name='memleket')),
                ('old', models.CharField(choices=[('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('11', 11), ('12', 12), ('13', 13), ('14', 14), ('15', 15), ('16', 16), ('17', 17), ('18', 18), ('19', 19), ('20', 20), ('21', 21), ('22', 22), ('23', 23), ('24', 24), ('25', 25), ('26', 26), ('27', 27), ('28', 28), ('29', 29), ('30', 30), ('31', 31), ('32', 32), ('33', 33), ('34', 34), ('35', 35), ('36', 36), ('37', 37), ('38', 38), ('39', 39), ('40', 40), ('41', 41), ('42', 42), ('43', 43), ('44', 44), ('45', 45), ('46', 46), ('47', 47), ('48', 48), ('49', 49), ('50', 50), ('51', 51), ('52', 52), ('53', 53), ('54', 54), ('55', 55), ('56', 56), ('57', 57), ('58', 58), ('59', 59), ('60', 60), ('61', 61), ('62', 62), ('63', 63), ('64', 64), ('65', 65), ('66', 66), ('67', 67), ('68', 68), ('69', 69), ('70', 70), ('71', 71), ('72', 72), ('73', 73), ('74', 74), ('75', 75), ('76', 76), ('77', 77), ('78', 78), ('79', 79), ('80', 80), ('81', 81), ('82', 82), ('83', 83), ('84', 84), ('85', 85), ('86', 86), ('87', 87), ('88', 88), ('89', 89), ('90', 90), ('91', 91), ('92', 92), ('93', 93), ('94', 94), ('95', 95), ('96', 96), ('97', 97), ('98', 98), ('99', 99), ('100', 100), ('101', 101), ('102', 102), ('103', 103), ('104', 104), ('105', 105), ('106', 106), ('107', 107), ('108', 108), ('109', 109)], max_length=4, verbose_name='Yaş')),
                ('university', models.CharField(choices=[('gaün', 'gaziantep')], max_length=20, null=True, verbose_name='üniversite')),
                ('jop', models.CharField(choices=[('student', 'öğrenci')], max_length=30, null=True, verbose_name='meslek')),
                ('iban', models.IntegerField(null=True, verbose_name='kart iban numarası')),
                ('phone', models.IntegerField(verbose_name='telefon numarası')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=37)),
                ('content_list', models.CharField(max_length=30, verbose_name='İçeriğinizin liste ismini yazın')),
                ('category', models.CharField(choices=[('ders', 'ders'), ('oyun', 'oyun'), ('seyahat', 'seyahat'), ('giyim', 'giyim'), ('makyaj-ve-cilt-bakm', 'makyaj ve cilt bakım'), ('saglk', 'sağlık'), ('yiyecek-ve-icecek', 'yiyecek ve içecek'), ('medya', 'medya'), ('urun-esya', 'ürün eşya'), ('tastlar', 'taşıtlar'), ('tannms-kisi', 'tanınmış kişi'), ('hayvanlar', 'hayvanlar'), ('inanc', 'inanç'), ('dil', 'dil'), ('metafizik', 'metafizik'), ('ask-arkadaslk', 'aşk arkadaşlık')], max_length=30, verbose_name='Kategori')),
                ('subcategory', models.CharField(blank=True, choices=[('gunluk-makyaj', 'Günlük Makyaj'), ('porselen-makyaj', 'Porselen Makyaj'), ('show-makyaj', 'Show Makyajı'), ('kalc-makyaj', 'Kalıcı Makyaj'), ('gece-makyaj', 'Gece Makyajı'), ('cilt-bakm', 'cilt bakımı'), ('sulu', 'sulu'), ('corbalar', 'çorbalar'), ('etli', 'etli'), ('fastfood', 'fastfood'), ('soguk', 'soğuk'), ('scak', 'sıcak'), ('alkollu', 'alkollu'), ('tatllar', 'tatlılar'), ('tuzlu', 'tuzlu'), ('restorant', 'restorant'), ('pasta', 'pasta'), ('ev-yemekleri', 'ev yemekleri'), ('televiyon-program', 'televiyon - program'), ('radyo', 'radyo'), ('sinema', 'sinema'), ('muzik', 'müzik'), ('kitap', 'kitap'), ('video', 'video'), ('ses', 'ses'), ('ev-esyalar', 'ev eşyaları'), ('teknolojik-esyalar', 'teknolojik eşyalar'), ('kara', 'kara'), ('hava', 'hava'), ('deniz', 'deniz'), ('bilim-insan', 'Bilim insanı'), ('siyaset-insan', 'siyaset insanı'), ('din-insan', 'din insanı'), ('felsefe-insan', 'felsefe insanı'), ('sinema-oyuncusu', 'sinema-oyuncusu'), ('muzisyen', 'müzisyen'), ('oyuncu-gamer', 'oyuncu - gamer'), ('yazar', 'yazar'), ('sarkc', 'şarkıcı'), ('sporcu', 'sporcu'), ('girisimci', 'girişimci'), ('diger', 'diğer'), ('sokak', 'sokak'), ('evcil', 'evcil'), ('vahsi', 'vahşi'), ('dini', 'dini'), ('kisisel', 'kişisel'), ('gunluk-makyaj', 'Günlük Makyaj'), ('porselen-makyaj', 'Porselen Makyaj'), ('show-makyaj', 'Show Makyajı'), ('kalc-makyaj', 'Kalıcı Makyaj'), ('gece-makyaj', 'Gece Makyajı'), ('cilt-bakm', 'cilt bakımı'), ('muhendislik', 'Mühendislik'), ('tp', 'Tıp'), ('fen-edebiyat', 'Fen edebiyat'), ('iktisadi-ve-idari-bilimleri', 'İktisadi ve idari bilimleri'), ('egitim', 'Eğitim'), ('dis-hekimligi', 'Diş hekimliği'), ('mimarlk', 'Mimarlık'), ('islahiye-iktisadi-ve-idari-bilimleri', 'İslahiye iktisadi ve idari bilimleri'), ('guzel-sanatlar', 'Güzel sanatlar'), ('saglk-bilimleri', 'Sağlık bilimleri'), ('hukuk', 'Hukuk'), ('ilahiyat', 'İlahiyat'), ('iletisim', 'İletişim'), ('havaclk-ve-uzay-muhendisligi', 'Havacılık ve uzay mühendisliği'), ('turizm', 'Turizm'), ('grand-theft-auto', 'grand theft auto'), ('counter-strike-global-offensive', 'counter strike global offensive'), ('euro-truck-simulator', 'euro truck simulator'), ('minecraft', 'minecraft'), ('fifa', 'fifa'), ('battlefield', 'battlefield'), ('call-of-duty', 'call of duty'), ('prey', 'prey'), ('watch-dogs', 'watch dogs'), ('fallout', 'fallout'), ('far-cry', 'far cry'), ('half-life', 'half-life'), ('assassins-creed', "assassin's creed"), ('league-of-legends', 'league of legends'), ('destiny', 'destiny'), ('rise-of-the-tomb-raider', 'rise of the tomb raider'), ('clash-of-clans', 'clash of clans'), ('adana', 'adana'), ('adyaman', 'adıyaman'), ('afyon', 'afyon'), ('agr', 'ağrı'), ('amasya', 'amasya'), ('ankara', 'ankara'), ('antalya', 'antalya'), ('artvin', 'artvin'), ('aydn', 'aydın'), ('balkesir', 'balıkesir'), ('bilecik', 'bilecik'), ('bingol', 'bingöl'), ('bitlis', 'bitlis'), ('bolu', 'bolu'), ('burdur', 'burdur'), ('bursa', 'bursa'), ('canakkale', 'çanakkale'), ('cankr', 'çankırı'), ('corum', 'çorum'), ('denizli', 'denizli'), ('diyarbakr', 'diyarbakır'), ('edirne', 'edirne'), ('elazg', 'elazığ'), ('erzincan', 'erzincan'), ('erzurum', 'erzurum'), ('eskisehir', 'eskişehir'), ('gaziantep', 'gaziantep'), ('giresun', 'giresun'), ('gumushane', 'gümüşhane'), ('hakkari', 'hakkari'), ('hatay', 'hatay'), ('sparta', 'ısparta'), ('mersin', 'mersin'), ('istanbul', 'istanbul'), ('izmir', 'izmir'), ('kars', 'kars'), ('kastamonu', 'kastamonu'), ('kayseri', 'kayseri'), ('krklareli', 'Kırklareli'), ('krsehir', 'kırşehir'), ('kocaeli', 'kocaeli'), ('konya', 'konya'), ('kutahya', 'kütahya'), ('malatya', 'malatya'), ('manisa', 'manisa'), ('kahramanmaras', 'kahramanmaraş'), ('mardin', 'mardin'), ('mugla', 'muğla'), ('mus', 'muş'), ('nevsehir', 'nevşehir'), ('nigde', 'niğde'), ('ordu', 'ordu'), ('rize', 'rize'), ('sakarya', 'sakarya'), ('samsun', 'samsun'), ('siirt', 'siirt'), ('sinop', 'sinop'), ('sivas', 'sivas'), ('tekirdag', 'tekirdağ'), ('tokat', 'tokat'), ('trabzon', 'trabzon'), ('tunceli', 'tunceli'), ('sanlurfa', 'şanlıurfa'), ('usak', 'uşak'), ('van', 'van'), ('yozgat', 'yozgat'), ('zonguldak', 'zonguldak'), ('aksaray', 'aksaray'), ('bayburt', 'bayburt'), ('karaman', 'karaman'), ('krkkale', 'kırıkkale'), ('batman', 'batman'), ('srnak', 'şırnak'), ('bartn', 'bartın'), ('ardahan', 'ardahan'), ('gdr', 'ığdır'), ('yalova', 'yalova'), ('karabuk', 'karabuk'), ('kilis', 'kilis'), ('osmaniye', 'osmaniye'), ('duzce', 'düzce'), ('yazlk', 'yazlık'), ('kslk', 'kışlık'), ('mevsimlik', 'mevsimlik'), ('aksesuar', 'aksesuar')], max_length=50, null=True, verbose_name='Alt kategori')),
                ('category2', models.CharField(blank=True, choices=[('makine', 'Makine'), ('elektrik-ve-elektronik', 'Elektrik ve elektronik'), ('gda', 'Gıda'), ('fizik', 'Fizik'), ('insaat', 'İnşaat'), ('tekstil', 'Tekstil'), ('endustri', 'Endüstri'), ('bigisayar', 'Bigisayar'), ('yazlm', 'Yazılım'), ('metalurji-ve-malzeme', 'Metalurji ve malzeme'), ('enerji-sistemleri', 'Enerji sistemleri'), ('biyoproses-ve-kimya', 'Biyoproses ve kimya'), ('optik-ve-akustik', 'Optik ve akustik'), ('dahili-tp-birimleri', 'Dahili tıp birimleri'), ('cerrahi-tp-birimleri', 'Cerrahi tıp birimleri'), ('temel-tp-birimleri', 'Temel tıp birimleri'), ('tarih', 'Tarih'), ('matematik', 'Matematik'), ('turk-dili-ve-edebiyat', 'Türk dili ve edebiyat'), ('biyoloji', 'Biyoloji'), ('bat-dilleri-ve-edebiyat', 'Batı dilleri ve edebiyat'), ('kimya', 'Kimya'), ('arkeoloji', 'Arkeoloji'), ('sosyoloji', 'Sosyoloji'), ('kultur-varlklarn-koruma-ve-onarm', 'Kültür varlıklarını koruma ve onarım'), ('istatislik', 'İstatislik'), ('psikoloji', 'Psikoloji'), ('cografya', 'Çoğrafya'), ('felsefe', 'Felsefe'), ('dogu-dilleri-ve-edebiyat', 'Doğu dilleri ve edebiyatı'), ('iktisat', 'İktisat'), ('isletme', 'İşletme'), ('uluslar-aras-ticaret-ve-lojistik', 'Uluslar arası ticaret ve lojistik'), ('kamu-yonetim', 'Kamu yönetim'), ('maliye', 'Maliye'), ('kuresel-siyaset-ve-uluslararas-iliskiler', 'Küresel siyaset ve uluslararası ilişkiler'), ('matematik-ve-fen-bilimleri', 'Matematik ve fen bilimleri'), ('guzel-sanatlar', 'Güzel sanatlar'), ('turkce-ve-sosyal-bilimler', 'Türkçe ve sosyal bilimler'), ('yabanc-diller', 'Yabancı diller'), ('egitim-yonetimi-anabilim-dal', 'Eğitim yönetimi anabilim dalı'), ('egitim-programlar-ve-ogretim-adabilim-dal', 'Eğitim programları ve öğretim adabilim dalı'), ('rehberlik-ve-psikojik-dansma-anabilim-dal', 'Rehberlik ve psikojik danışma anabilim dalı'), ('egitimin-felsefesisosyal-ve-tarihi-temelleri-anabilim-dal', 'Eğitimin felsefesi,sosyal ve tarihi temelleri anabilim dalı'), ('hayat-boyu-ogrenme-ve-yetiskin-egitimi-anabilim-dal', 'Hayat boyu öğrenme ve yetişkin eğitimi anabilim dalı'), ('ogretim-teknolojileri-anabilim-dal', 'Öğretim teknolojileri anabilim dalı'), ('egitimde-olcme-ve-degerlendirme-anabilim-dal', 'Eğitimde ölçme ve değerlendirme anabilim dalı'), ('bilgisayar-ve-ogretim-teknolojileri', 'Bilgisayar ve öğretim teknolojileri'), ('okul-oncesi-egitimi-anabilim-dal', 'Okul öncesi eğitimi anabilim dalı'), ('snf-egitimi-anabilim-dal', 'Sınıf eğitimi anabilim dalı'), ('ozel-yetenekliler-egitimi-anabilim-dal', 'Özel yetenekliler eğitimi anabilim dalı'), ('zihinsel-engelliler-egitimi-anabilim-dal', 'Zihinsel engelliler eğitimi anabilim dalı'), ('gorme-engelliler-egitimi-anabilim-dal', 'Görme engelliler eğitimi anabilim dalı'), ('isitme-engelliler-egitimi-anabilim-dal', 'İşitme engelliler eğitimi anabilim dalı'), ('egitimi-anabilim-dal', 'eğitimi anabilim dalı'), ('agz-dis-ve-cene-cerrahisi-ad', 'Ağız Diş ve Çene Cerrahisi AD.'), ('endodonti-ad', 'Endodonti AD.'), ('oral-diagnoz-ve-radyoloji-ad', 'Oral Diagnoz ve Radyoloji AD.'), ('ortodonti-ad', 'Ortodonti AD.'), ('pedodonti-ad', 'Pedodonti AD.'), ('periodontoloji-ad', 'Periodontoloji AD.'), ('protetik-dis-tedavisi-ad', 'Protetik Diş Tedavisi AD.'), ('restoratif-dis-tedavisi-ad', 'Restoratif Diş Tedavisi AD.'), ('sehir-ve-bolge-planlama-bolumu', 'ŞEHİR VE BÖLGE PLANLAMA BÖLÜMÜ'), ('endustri-urunleri-tasarimi-bolumu', 'ENDÜSTRİ ÜRÜNLERİ TASARIMI BÖLÜMÜ'), ('mimarlik-bolumu', 'MİMARLIK BÖLÜMÜ'), ('ic-mimarlik-bolumu', 'İÇ MİMARLIK BÖLÜMÜ'), ('ekonometri', 'EKONOMETRİ'), ('uluslararasi-iliskiler', 'ULUSLARARASI İLİŞKİLER'), ('maliye', 'MALİYE'), ('kamu-yonetimi', 'KAMU YÖNETİMİ'), ('iktisat', 'İKTİSAT'), ('isletme', 'İŞLETME'), ('gastronomi-ve-mutfak-sanatlari-bolumu', 'GASTRONOMİ VE MUTFAK SANATLARI BÖLÜMÜ'), ('moda-ve-tekstil-tasarimi-bolumu', 'MODA VE TEKSTİL TASARIMI BÖLÜMÜ'), ('sahne-ve-gosteri-sanatlari-bolumu', 'SAHNE VE GÖSTERİ SANATLARI BÖLÜMÜ'), ('geleneksel-turk-el-sanatlari-bolumu', 'GELENEKSEL TÜRK EL SANATLARI BÖLÜMÜ'), ('sinema-ve-televizyon-bolumu', 'SİNEMA VE TELEVİZYON BÖLÜMÜ'), ('fotograf-bolumu', 'FOTOĞRAF BÖLÜMÜ'), ('seramik-ve-cam-bolumu', 'SERAMİK VE CAM BÖLÜMÜ'), ('resim-bolumu', 'RESİM BÖLÜMÜ'), ('heykel-bolumu', 'HEYKEL BÖLÜMÜ'), ('grafik-bolumu', 'GRAFİK BÖLÜMÜ'), ('fizyoterapi-ve-rehabilitasyon', 'FİZYOTERAPİ VE REHABİLİTASYON'), ('dil-ve-konusma-terapisi', 'DİL VE KONUŞMA TERAPİSİ'), ('odyoloji', 'ODYOLOJİ'), ('beslenme-ve-diyetetik', 'BESLENME VE DİYETETİK'), ('saglik-yonetimi', 'SAĞLIK YÖNETİMİ'), ('solunum-terapistligi', 'SOLUNUM TERAPİSTLİĞİ'), ('ebelik', 'EBELİK'), ('hemsirelik', 'HEMŞİRELİK'), ('hukuk-fakultesi', 'HUKUK FAKÜLTESİ'), ('anayasa-hukuku-anabilim-dali', 'ANAYASA HUKUKU ANABİLİM DALI'), ('ceza-ve-ceza-muhakemesi-hukuku-anabilim-dali', 'CEZA VE CEZA MUHAKEMESİ HUKUKU ANABİLİM DALI'), ('genel-kamu-hukuku-anabilim-dali', 'GENEL KAMU HUKUKU ANABİLİM DALI'), ('hukuk-felsefesi-ve-sosyolojisi-anabilim-dali', 'HUKUK FELSEFESİ VE SOSYOLOJİSİ ANABİLİM DALI'), ('hukuk-tarihi-anabilim-dali', 'HUKUK TARİHİ ANABİLİM DALI'), ('mali-hukuk-anabilim-dali', 'MALİ HUKUK ANABİLİM DALI'), ('milletlerarasi-hukuk-anabilim-dali', 'MİLLETLERARASI HUKUK ANABİLİM DALI'), ('idare-hukuku-anabilim-dali', 'İDARE HUKUKU ANABİLİM DALI'), ('insan-haklari-anabilim-dali', 'İNSAN HAKLARI ANABİLİM DALI'), ('islam-hukuku-anabilim-dali', 'İSLAM HUKUKU ANABİLİM DALI'), ('ticaret-hukuku-anabilim-dali', 'TİCARET HUKUKU ANABİLİM DALI'), ('avrupa-birligi-hukuku-anabilim-dali', 'AVRUPA BİRLİĞİ HUKUKU ANABİLİM DALI'), ('deniz-hukuku-anabilim-dali', 'DENİZ HUKUKU ANABİLİM DALI'), ('karsilastirmali-hukuk-anabilim-dali', 'KARŞILAŞTIRMALI HUKUK ANABİLİM DALI'), ('medeni-hukuk-anabilim-dali', 'MEDENİ HUKUK ANABİLİM DALI'), ('medeni-usul-ve-icra-iflas-hukuku-anabilim-dali', 'MEDENİ USUL VE İCRA İFLAS HUKUKU ANABİLİM DALI'), ('milletlerarasi-ozel-hukuk-anabilim-dali', 'MİLLETLERARASI ÖZEL HUKUK ANABİLİM DALI'), ('roma-hukuku-anabilim-dali', 'ROMA HUKUKU ANABİLİM DALI'), ('is-ve-sosyal-guvenlik-hukuku-anabilim-dali', 'İŞ VE SOSYAL GÜVENLİK HUKUKU ANABİLİM DALI'), ('tefsir', 'Tefsir'), ('hadis', 'Hadis'), ('kelam', 'Kelam'), ('islam-hukuku', 'İslam Hukuku'), ('islam-mezhepleri-tarihi', 'İslam Mezhepleri Tarihi'), ('tasavvuf', 'Tasavvuf'), ('arap-dili-ve-belagat', 'Arap Dili ve Belagatı'), ('kuran-kerim-okuma-ve-kraat-ilmi', 'Kuranı Kerim Okuma ve Kıraat İlmi'), ('din-egitimi', 'Din Eğitimi'), ('dinler-tarihi', 'Dinler Tarihi'), ('islam-felsefesi', 'İslam Felsefesi'), ('din-sosyolojisi', 'Din Sosyolojisi'), ('din-psikolojisi', 'Din Psikolojisi'), ('felsefe-tarihi', 'Felsefe Tarihi'), ('mantk', 'Mantık'), ('islam-tarihi', 'İslam Tarihi'), ('turk-islam-edebiyat', 'Türk İslam Edebiyatı'), ('turk-islam-sanatlar-tarihi', 'Türk İslam Sanatları Tarihi'), ('turk-din-musikisi', 'Türk Din Musikisi'), ('gazetecilik', 'Gazetecilik'), ('halkla-iliskiler-ve-tantm', 'Halkla ilişkiler ve tanıtım'), ('radyo-tv-ve-sinema', 'Radyo, tv ve sinema'), ('iletisim-enformatigi', 'İletişim enformatiği'), ('reklamclk', 'Reklamcılık'), ('havacilik-yonetimi-bolumu', 'HAVACILIK YÖNETİMİ BÖLÜMÜ'), ('ucak-ve-uzay-muhendisligi-bolumu', 'UÇAK VE UZAY MÜHENDİSLİĞİ BÖLÜMÜ'), ('pilotaj-bolumu', 'PİLOTAJ BÖLÜMÜ')], max_length=80, null=True, verbose_name='İkinci alt kategori')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık yazın')),
                ('url', models.SlugField(max_length=100, unique=True, verbose_name='Web adresi, başlık ile aynı olmasına özen gösterin ')),
                ('content', ckeditor.fields.RichTextField(verbose_name='içeriğinizi oluşturun')),
                ('tag', models.CharField(max_length=200, verbose_name='İçeriğiniz ili ilgili anahtar kelimeleri virgul kullanarak yazın')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='tarih')),
                ('dor', models.TextField()),
                ('stars', models.IntegerField(default=0, verbose_name='Yıldız')),
                ('hmstars', models.IntegerField(default=0, verbose_name='kaç kişi oy kullandı')),
            ],
            options={
                'verbose_name': 'content',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='ContentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=37)),
                ('content_list', models.SlugField(max_length=30, verbose_name='İçerik listeniz')),
                ('content_count', models.IntegerField(verbose_name='liste içindeki nesne sayısı')),
            ],
        ),
        migrations.CreateModel(
            name='OtherInformationOfUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp', models.BooleanField(verbose_name='profil resmi yüklemiş mi ?')),
                ('is_author', models.BooleanField(verbose_name='yazar olarak kabul et')),
                ('author', models.BooleanField(verbose_name='yazarlık başvurusu yaptımı')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Voters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_id', models.IntegerField()),
                ('blog_id', models.IntegerField(verbose_name='hangi blog')),
                ('star', models.IntegerField(default=0, verbose_name='Yıldız')),
            ],
        ),
    ]
