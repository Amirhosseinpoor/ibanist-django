import re
pishshomare_bank = {
        '055': 'bank eghtesad novin',
        '054': 'bank parsian',
        '057': 'bank pasargad',
        '021': 'post bank iran',
        '018': 'bank tejarat',
        '051': 'moasese etebari tosee',
        '020': 'bank tosee saaderat',
        '013': 'bank refah',
        '056': 'bank saman',
        '015': 'bank sepah',
        '058': 'bank sarmaye',
        '019': 'bank saderat iran',
        '011': 'bank sanaat va madan',
        '053': 'bank kar afarin',
        '016': 'bank keshavarzi',
        '010': 'bank markazi jomhori eslami iran',
        '014': 'bank maskan',
        '012': 'bank melat',
        '017': 'bank meli iran',
        '065': 'bank hekmat',
        '062': 'bank ayandeh',
        '061': 'bank shahr',
        '066': 'bank dey',
        '078': 'bank khavarmiane',
        '063': 'bank ansar',
        '069': 'bank  iranzamin',
        '022': 'bank tosee va taavon',
        '064': 'bank gardeshgari',
        '070': 'bank resalat',
        '059': 'bank sina',
        '052': 'bank ghavamin',
        '080': 'bank noor',
        '060': 'bank mehriran',
        '079': 'bank mehreghtesad',
        '': ''

}

bank_pishshomare = {
        'bank eghtesad novin': '055',
        'bank parsian': '054',
        'bank pasargad': '057',
        'post bank iran': '021',
        'bank tejarat': '018',
        'moasese etebari tosee': '051',
        'bank tosee saaderat': '020',
        'bank refah': '013',
        'bank saman': '056',
        'bank sepah': '015',
        'bank sarmaye': '058',
        'bank saderat iran': '019',
        'bank sanaat va madan': '011',
        'bank kar afarin': '053',
        'bank keshavarzi': '016',
        'bank markazi jomhori eslami iran': '010',
        'bank maskan': '014',
        'bank melat': '012',
        'bank meli iran': '017',
        'bank hekmat': '065',
        'bank ayandeh': '062',
        'bank shahr': '061',
        'bank dey': '066',
        'bank khavarmiane': '078',
        'bank ansar': '063',
        'bank  iranzamin': '069',
        'bank tosee va taavon': '022',
        'bank gardeshgari': '064',
        'bank resalat': '070',
        'bank sina': '059',
        'bank ghavamin': '052',
        'bank noor': '080',
        'bank mehriran': '060',
        'bank mehreghtesad': '079',
        '': ''
}
num_bunk = {
         '1': 'bank keshavarzi', '2': 'bank tejarat', '3': 'bank refah', '4': 'bank saderat iran',
         '5': 'bank parsian', '6': 'bank mehriran', '7': 'bank meli iran', '8': 'bank melat', '9': 'bank sepah',
         '': ''
}





class Ibanist:
    def __init__(self, iban='', an='', bank='', accounttype=''):
        self.valid = False
        if an != '':
            self.valid = True
        self.accountype = accounttype
        self.iban = iban
        self.an = an
        self.bi = bank_pishshomare[num_bunk[bank]]
        self.bank, self.an = self.parse(self.iban)
        self.truth(self.iban, self.bank, self.an)

    def __str__(self):
        return {"iban": self.iban, "bank": self.bank, "an": self.an}

    def truth(self, iban, bank, an):
        iban_realnumber = self.real_number(iban)
        iban_realnumber_ir = iban_realnumber + '1827'
        cd = iban_realnumber[0:2]
        iban_realnumber_ir_cd = iban_realnumber_ir + cd
        iban_realnumber_ir_cd = re.sub(r'^..', '', iban_realnumber_ir_cd)

        if int(iban_realnumber_ir_cd) % 97 == 1 and len(iban_realnumber) == 24:
            self.bank = bank
            self.iban = iban
            self.an = an
            # print(f'{self.iban} {self.bank} {self.an}')
        else:
            self.bank = 'invalid'
            self.iban = 'invalid'
            self.an = 'invalid'
            # print(f'{self.iban} {self.bank} {self.an}')

    def parse(self, iban):
        global bank
        cc = 'IR'
        if self.valid:
            bi = self.bi
            an = self.real_number(self.an)

        else:
            bi = self.real_number(iban)[2:5]
            an = self.real_number(iban)[5:]
            an = re.sub(r'^0+', '', an)
        try:
            bank = pishshomare_bank[bi]
        except KeyError:
            return "invalid"
        match bi:

            case '016':  # bank keshavarzi
                if len(an) == 9:
                    an = '0' + an
                self.bank_keshavarzi(cc, bi, an)

            case '018':  # bank tejarat
                if len(an) == 9:
                    an = '0' + an
                self.bank_tejarat(cc, bi, an)

            case '013':  # bank refah
                an = re.sub(r'^1', '', an)
                an = re.sub(r'^0+', '', an)
                if len(an) == 9:
                    an = '0' + an
                self.bank_refah(cc, bi, an)

            case '019':  # bank saderat
                if len(an) == 12:
                    an = '0' + an
                self.bank_saderat(cc, bi, an)

            case '054':  # bank parsian
                an = re.sub(r'1219', '', an)
                self.bank_parsian(cc, bi, an)

            case '060':  # bank mehriran
                if self.iban != '':
                    if self.an != '':
                        pass
                    else:
                        an = an[:-3] + an[-1]
                self.bank_mehriran(cc, bi, an)

            case '017':  # bank meli
                if len(an) == 12:
                    an = '0' + an
                self.bank_meli(cc, bi, an, self.accountype)

            case '012':  # bank melat
                an = re.sub(r'^1', '', an)
                an = re.sub(r'^0+', '', an)
                an = re.sub(r'^2', '', an)
                an = re.sub(r'^0+', '', an)
                self.bank_melat(cc, bi, an, self.accountype)

            case '015':  # bank sepah
                if len(an) == 12:
                    an = '0' + an
                self.bank_sepah(cc, bi, an)

        return bank, an

    def real_number(self, num):
        num = re.sub(r' ', '', num)
        num = re.sub(r'-', '', num)
        num = re.sub(r'_', '', num)
        num = re.sub(r'IR', '', num)
        num = re.sub(r'Ir', '', num)
        num = re.sub(r'iR', '', num)
        num = re.sub(r'ir', '', num)
        return num

    def bank_keshavarzi(self, cc, bi, an):
        an = re.sub(r' ', '', an)
        if len(an) == 9:
            an = '0' + an
        bban = bi + "000000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_tejarat(self, cc, bi, an):
        an = re.sub(r' ', '', an)
        if len(an) == 9:
            an = '0' + an
        bban = bi + "000000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_refah(self, cc, bi, an):
        an = re.sub(r' ', '', an)

        if len(an) == 9:
            an = '0' + an
        bban = bi + "010000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_saderat(self, cc, bi, an):
        an = re.sub(r' ', '', an)

        if len(an) == 12:
            an = '0' + an
        bban = bi + "000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_parsian(self, cc, bi, an):
        an = re.sub(r' ', '', an)

        bban = bi + "01219" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_mehriran(self, cc, bi, an):
        an = re.sub(r' ', '', an)

        bban = bi + "0" + str(an)[:-1] + "00" + str(an)[-1]

        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_melat(self, cc, bi, an, accounttype='1'):
        global bban
        an = re.sub(r' ', '', an)

        if accounttype == "1":
            bban = bi + "000000000" + str(an)
        elif accounttype == "2":
            bban = bi + "001000000" + str(an)
        elif accounttype == "3":
            bban = bi + "002000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_meli(self, cc, bi, an, accounttype='1'):
        global bban
        an = re.sub(r' ', '', an)

        if len(an) == 12:
            an = '0' + an
        if accounttype == "1":
            # sepordeh
            bban = bi + "000000" + str(an)
        elif accounttype == "2":
            # tashilat
            bban = bi + "10000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_sepah(self, cc, bi, an):
        an = re.sub(r' ', '', an)
        if len(an) == 12:
            an = '0' + an
        bban = bi + "000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

# '1': 'bank keshavarzi', '2': 'bank tejarat', '3': 'bank refah', '4': 'bank saderat iran',
#         '5': 'bank parsian', '6': 'bank mehriran', '7': 'bank meli iran', '8': 'bank melat',

print(Ibanist(an='3019025140830361', bank='6').__str__()["iban"])
Ibanist(iban='IR570600301902514083036001', bank='6', an='3019025140830361')
