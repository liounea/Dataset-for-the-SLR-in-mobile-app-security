import csv

# Ouvrir le fichier csv d'entrée
with open("path/to/file/containing/the/publictions_to_filter.csv", 'r', encoding='utf-8') as input_file:
    # Créer le lecteur csv
    reader = csv.DictReader(input_file)

    # Ouvrir le fichier csv de sortie
    with open("path/to/file/containing/the/results.csv", 'a', encoding='utf-8', newline='') as output_file:
        # Créer le writer csv avec les mêmes entêtes que le fichier d'entrée
        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
        writer.writeheader()

        # Parcourir chaque ligne du fichier d'entrée
        for row in reader:
            # Récupérer les valeurs de 'Document Title' et 'Abstract'
            document_title = row['Document Title']
            abstract = row['Abstract']

            # Vérifier si les conditions sont remplies pour inclure la ligne
            if (('android' in document_title.lower() or 'mobile' in document_title.lower() or 'smartphone' in document_title.lower() or
                'smart phone' in document_title.lower() or 'iphone' in document_title.lower() or
                'ios' in document_title.lower() or 'portable device' in document_title.lower() or 'app' in document_title.lower()) and \
                 ('security' in document_title.lower() or 'malware' in document_title.lower() or
                'vulnerabilit' in document_title.lower() or 'weak' in document_title.lower() or 'exploit' in document_title.lower() or
                'flaw' in document_title.lower() or 'breach' in document_title.lower() or 'leak' in document_title.lower() or
                'malicious' in document_title.lower() or 'phishing' in document_title.lower() or 'ransomware' in document_title.lower() or
                'trojan' in document_title.lower() or 'attack' in document_title.lower() or 'compliance' in document_title.lower() or
                'crypto' in document_title.lower() or 'forensic' in document_title.lower() or 'reverse engineering' in document_title.lower() or
                'encryption' in document_title.lower() or 'threat' in document_title.lower() or 'hack*' in document_title.lower() or 'privacy violation' in document_title.lower()) and \
                    ('Egypt' in document_title or 'Libya' in document_title or
                     'Angola' in document_title or
                     'Benin' in document_title or 'Botswana' in document_title or 'Burkina Faso' in document_title or
                     'Burundi' in document_title or 'Cameroon' in document_title or 'Cabo Verde' in document_title or
                     'Central African Republic' in document_title or 'Chad' in document_title or 'Comoros' in document_title or
                     'Congo' in document_title or 'Ivory coast' in document_title or 'Djibouti' in document_title or
                     'St. Helena' in document_title or 'Eritrea' in document_title or 'Eswatini' in document_title or
                     'Ethiopia' in document_title or 'Gabon' in document_title or 'Gambia' in document_title or
                     'Ghana' in document_title or 'Guinea' in document_title or 'Kenya' in document_title or
                     'Lesotho' in document_title or 'Liberia' in document_title or 'Madagascar' in document_title or
                     'Malawi' in document_title or 'Mali' in document_title or 'Mauritania' in document_title or
                     'Mauritius' in document_title or 'Mozambique' in document_title or 'Namibia' in document_title or
                     'Niger' in document_title or 'Sao Tome & Principe' in document_title or 'Rwanda' in document_title or
                     'Senegal' in document_title or 'Sierra Leone' in document_title or 'Somalia' in document_title or
                     'Sudan' in document_title or 'Tanzania' in document_title or 'Uganda' in document_title or
                     'Togo' in document_title or 'Zambia' in document_title or 'Zimbabwe' in document_title or
                     'Albania' in document_title or 'Armenia' in document_title or 'Azerbaijan' in document_title or
                     'Belarus' in document_title or 'Bosnia Herzegovina' in document_title or 'Georgia' in document_title or
                     'Kosovo' in document_title or 'Macedonia' in document_title or
                     'Moldova' in document_title or 'Montenegro' in document_title or 'Serbia' in document_title or
                     'Ukraine' in document_title or 'Belize' in document_title or
                     'Costa Rica' in document_title or 'Cuba' in document_title or 'Dominica' in document_title or
                     'El Salvador' in document_title or 'Grenada' in document_title or 'Guatemala' in document_title or
                     'Haiti' in document_title or 'Honduras' in document_title or 'Jamaica' in document_title or
                     'Montserrat' in document_title or 'Nicaragua' in document_title or
                     'Panama' in document_title or 'St. Lucia' in document_title or 'St. Vincent and the Grenadines' in document_title or
                     'Bolivia' in document_title or 'Ecuador' in document_title or 'Guyana' in document_title or
                     'Paraguay' in document_title or 'Peru' in document_title or 'Suriname' in document_title or
                     'Venezuela' in document_title or 'Afghanistan' in document_title or 'Bhutan' in document_title or 'Cambodia' in document_title or
                     'Kyrgyzstan' in document_title or "Lao People’s Democratic Republic" in document_title or
                     'Maldives' in document_title or 'Mongolia' in document_title or
                     'Myanmar' in document_title or 'Nepal' in document_title or 'Pakistan' in document_title or
                     'Tajikistan' in document_title or 'Timor Leste' in document_title or 'Turkmenistan' in document_title or
                     'Uzbekistan' in document_title or 'Iraq' in document_title or 'Jordan' in document_title or 'Lebanon' in document_title or
                     'Syrian Arab Republic' in document_title or 'West Bank and Gaza Strip' in document_title or
                     'Yemen' in document_title or 'Cook Islands' in document_title or 'Fiji' in document_title or
                     'Kiribati' in document_title or 'Marshall Islands' in document_title or 'Micronesia' in document_title or
                     'Nauru' in document_title or
                     'Niue' in document_title or
                     'Palau' in document_title or
                     'Samoa' in document_title or
                     'Solomon Islands' in document_title or
                     'Tokelau' in document_title or
                     'Tonga' in document_title or
                     'Tuvalu' in document_title or
                     'Vanuatu' in document_title or
                     'Wallis & Futuna' in document_title or 'Wallis and Futuna' in document_title or
                     'developing countr' in document_title.lower() or
                     'developing world' in document_title.lower() or
                     'low-income countr' in document_title.lower() or
                     'middle-income countr' in document_title.lower() or
                     'Africa' in document_title or
                     'south asia' in document_title.lower() or
                     'least-developed countr' in document_title.lower())) or \
                (('android' in abstract.lower() or 'mobile' in abstract.lower() or 'smartphone' in abstract.lower() or
                'smart phone' in abstract.lower() or 'iphone' in abstract.lower() or
                'ios' in abstract.lower() or 'portable device' in abstract.lower() or 'app' in abstract.lower()) and \
                 ('security' in abstract.lower() or 'malware' in abstract.lower() or
                'vulnerabilit' in abstract.lower() or 'weak' in abstract.lower() or 'exploit' in abstract.lower() or
                'flaw' in abstract.lower() or 'breach' in abstract.lower() or 'leak' in abstract.lower() or
                'malicious' in abstract.lower() or 'phishing' in abstract.lower() or 'ransomware' in abstract.lower() or
                'trojan' in abstract.lower() or 'attack' in abstract.lower() or 'compliance' in abstract.lower() or
                'crypto' in abstract.lower() or 'forensic' in abstract.lower() or 'reverse engineering' in abstract.lower() or
                'encryption' in abstract.lower() or 'threat' in abstract.lower() or 'hack*' in abstract.lower() or 'privacy violation' in abstract.lower()) and \
                    ('Egypt' in abstract or 'Libya' in abstract or
                     'Angola' in abstract or
                     'Benin' in abstract or 'Botswana' in abstract or 'Burkina Faso' in abstract or
                     'Burundi' in abstract or 'Cameroon' in abstract or 'Cabo Verde' in abstract or
                     'Central African Republic' in abstract or 'Chad' in abstract or 'Comoros' in abstract or
                     'Congo' in abstract or 'Ivory coast' in abstract or 'Djibouti' in abstract or
                     'St. Helena' in abstract or 'Eritrea' in abstract or 'Eswatini' in abstract or
                     'Ethiopia' in abstract or 'Gabon' in abstract or 'Gambia' in abstract or
                     'Ghana' in abstract or 'Guinea' in abstract or 'Kenya' in abstract or
                     'Lesotho' in abstract or 'Liberia' in abstract or 'Madagascar' in abstract or
                     'Malawi' in abstract or 'Mali' in abstract or 'Mauritania' in abstract or
                     'Mauritius' in abstract or 'Mozambique' in abstract or 'Namibia' in abstract or
                     'Niger' in abstract or 'Sao Tome & Principe' in abstract or 'Rwanda' in abstract or
                     'Senegal' in abstract or 'Sierra Leone' in abstract or 'Somalia' in abstract or
                     'Sudan' in abstract or 'Tanzania' in abstract or 'Uganda' in abstract or
                     'Togo' in abstract or 'Zambia' in abstract or 'Zimbabwe' in abstract or
                     'Albania' in abstract or 'Armenia' in abstract or 'Azerbaijan' in abstract or
                     'Belarus' in abstract or 'Bosnia Herzegovina' in abstract or 'Georgia' in abstract or
                     'Kosovo' in abstract or 'Macedonia' in abstract or
                     'Moldova' in abstract or 'Montenegro' in abstract or 'Serbia' in abstract or
                     'Ukraine' in abstract or 'Belize' in abstract or
                     'Costa Rica' in abstract or 'Cuba' in abstract or 'Dominica' in abstract or
                     'El Salvador' in abstract or 'Grenada' in abstract or 'Guatemala' in abstract or
                     'Haiti' in abstract or 'Honduras' in abstract or 'Jamaica' in abstract or
                     'Montserrat' in abstract or 'Nicaragua' in abstract or
                     'Panama' in abstract or 'St. Lucia' in abstract or 'St. Vincent and the Grenadines' in abstract or
                     'Bolivia' in abstract or 'Ecuador' in abstract or 'Guyana' in abstract or
                     'Paraguay' in abstract or 'Peru' in abstract or 'Suriname' in abstract or
                     'Venezuela' in abstract or 'Afghanistan' in abstract or 'Bhutan' in abstract or 'Cambodia' in abstract or
                     'Kyrgyzstan' in abstract or "Lao People’s Democratic Republic" in abstract or
                     'Maldives' in abstract or 'Mongolia' in abstract or
                     'Myanmar' in abstract or 'Nepal' in abstract or 'Pakistan' in abstract or
                     'Tajikistan' in abstract or 'Timor Leste' in abstract or 'Turkmenistan' in abstract or
                     'Uzbekistan' in abstract or 'Iraq' in abstract or 'Jordan' in abstract or 'Lebanon' in abstract or
                     'Syrian Arab Republic' in abstract or 'West Bank and Gaza Strip' in abstract or
                     'Yemen' in abstract or 'Cook Islands' in abstract or 'Fiji' in abstract or
                     'Kiribati' in abstract or 'Marshall Islands' in abstract or 'Micronesia' in abstract or
                     'Nauru' in abstract or
                     'Niue' in abstract or
                     'Palau' in abstract or
                     'Samoa' in abstract or
                     'Solomon Islands' in abstract or
                     'Tokelau' in abstract or
                     'Tonga' in abstract or
                     'Tuvalu' in abstract or
                     'Vanuatu' in abstract or
                     'Wallis & Futuna' in abstract or 'Wallis and Futuna' in abstract or
                     'developing countr' in abstract.lower() or
                     'developing world' in abstract.lower() or
                     'low-income countr' in abstract.lower() or
                     'middle-income countr' in abstract.lower() or
                     'Africa' in abstract or
                     'south asia' in abstract.lower() or
                     'least-developed countr' in abstract.lower())):
                writer.writerow(row)
