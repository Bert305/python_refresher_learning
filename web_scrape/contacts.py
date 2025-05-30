import re
import csv

# Raw input string (you can replace this with reading from a file or other input method)
raw_data = """
Alves, Lisette M. <LAlves@dadeschools.net>; Aponte, Yesenia M. <YAponte@dadeschools.net>; Villalobos, Rafael A. <VillalobosR@Dadeschools.net>; Swain, Brenda L. <bswain@dadeschools.net>; Mendizabal, Barbara A. <bmendizabal@dadeschools.net>; CHAVARRIA, JACQUELINE E <jchavarria@dadeschools.net>; Fox, Reginald J. <rfox@dadeschools.net>; Harris, Martha Z. <mharris1@dadeschools.net>; Carranza, Cristian <ccarranza1@dadeschools.net>; Diaz, Lupe F. <lupediaz@dadeschools.net>; Krantz, Sharon S. <skrantz@dadeschools.net>; Uriarte, Wirthy E. <WFuentes@dadeschools.net>; VALDES GONZALEZ, LISET <liset@dadeschools.net>; Jadoonandan, Indira M. <m-jadoo@dadeschools.net>; ST FLEUR, FABIENNE <stfleur@dadeschools.net>; Castro, Bibiana S. <bibianacastro@dadeschools.net>; HOLMES, RANDALL L <rholmes@dadeschools.net>; Jackson, Anthenisia A. <aajackson@dadeschools.net>; Mitchell, Carlena M. <169982@dadeschools.net>; Styles, Latosha T. <LStyles@dadeschools.net>; Suarez, Nelson <NSuarez@dadeschools.net>; Gutierrez, Maria D. <mdgutierrez@dadeschools.net>; Lambo, Yessenia L. <ylambo@dadeschools.net>; Mauri, Susana <smauri@dadeschools.net>; Fox, Reginald J. <rfox@dadeschools.net>; Bowers, Patsy A. <pbowers@dadeschools.net>; CHAVARRIA, JACQUELINE E <jchavarria@dadeschools.net>; CHOZO, ALVARO M <achozo@dadeschools.net>; CHUNG GRANT, BEVERLY <311063@dadeschools.net>; Diaz-Duque, Rosy <rosydd@dadeschools.net>; Evans, Erica N. <eevans1@dadeschools.net>; Ferro, Alnerys <aferro@dadeschools.net>; FLOR, ESTHER <EFlor@dadeschools.net>; Santa Cruz, Guillermo <gsantacruz@homesteadmiamispeedway.com>; Gray, Sharon A. <graysharona@dadeschools.net>; Marti, Sergio A. <smarti@dadeschools.net>; Morejon, Elena <elenam@dadeschools.net>; WATKINS, JACOBY <watkinsj@dadeschools.net>; Whiting, Robart A. <whitingr@dadeschools.net>; Caldwell, Ericka H. <ecaldwell@dadeschools.net>; Davis, Barto G. <btdavis@dadeschools.net>; Parker, Scott E. <sparker@dadeschools.net>; PINELL, MARTHA S <marthapinell@dadeschools.net>; Gutierrez, Maria D. <mdgutierrez@dadeschools.net>; Molliner, Eduardo A. <206199@dadeschools.net>; 94thaeroclaimsgroup@gmail.com; Lisa Martinez <lisa@lmgenuinesolutions.com>; Mitchell, Carlena M. <169982@dadeschools.net>; Beasley, Roderick [CareerSource] <rick.beasley@careersourcesfl.com>; Santa Cruz, Guillermo <gsantacruz@homesteadmiamispeedway.com>; Collman, Cadian <collman@dadeschools.net>; Fox, Unethia V. <unethiafox@dadeschools.net>; PORTUONDO, SHANNON M <sportuondo@dadeschools.net>; Beasley, Roderick (Rick) (Career Source) <RoderickRick.Beasley@miamidade.gov>; Owens, Elizabeth (Seaport) <Elizabeth.Owens@miamidade.gov>; Jarvis Washington <Jarvis.Washington@careersourcesfl.com>; Porro, William (CAHSD) <William.Porro@miamidade.gov>; DELGADO, CRISTINA D <cdcdelgado@dadeschools.net>; RAMIREZ, ALEXANDRE <AlexRamirez@dadeschools.net>; TONK, MAHATI <mtonk@dadeschools.net>; Cone, Steffond L. <SLCONE@dadeschools.net>; HOLMES, RANDALL L <rholmes@dadeschools.net>; THOMAS, CHARLENE M <335663@dadeschools.net>; LANUZA, IVANIA <331162@dadeschools.net>; MOREIRA, LAZARO <L.Moreira@dadeschools.net>; WILLIAMS, PHILLIP <Diesel@dadeschools.net>; PORTUONDO, AMADO F <Afportuondo@dadeschools.net>; VALDES GONZALEZ, LISET <liset@dadeschools.net>; Rachel Ludwig <rludwig@flchamber.com>; Gonzalez, Ernesto F. <ernestogonzalez@dadeschools.net>; Allen, Jason H. <jallen23@dadeschools.net>; Latus, Melissa A. <MLatus@dadeschools.net>; BALSEIRO, MONTSERRAT <mbalseiro@dadeschools.net>; Cervantes, Maria B. <MCervantes@dadeschools.net>; Hidalgo, Georgina M. <ginakoch@dadeschools.net>; joe.chan@gm.com; joechi888@camacol.org; Zuanel Diaz: <zuaneld@baptisthealth.net>; Rachel Ludwig <rludwig@flchamber.com>; arachmell@purdueglobal.edu; shansel@chapmanpartnership.org; apaz@chapmanpartnership.org; Eddie Garza <ceo@mexamcouncil.org>; Beasley, Roderick [CareerSource] <rick.beasley@careersourcesfl.com>; Beasley, Roderick (Rick) (Career Source) <roderickrick.beasley@miamidade.gov>; Porro, William (CAHSD) <william.porro@miamidade.gov>; Mantilla, Rene <RMantilla@dadeschools.net>; Mendizabal, Barbara A. <bmendizabal@dadeschools.net>
Dotres, Jose L. <JDotres@Dadeschools.net>; Lewis, Michael A. <MJLEWIS@dadeschools.net>; Baglos, Dawn M. <dbaglos@dadeschools.net>; Bueno, Jose <jbueno@dadeschools.net>; Diaz, Luis E. <LDiaz21@dadeschools.net>; Diaz, Lourdes <lmcela@dadeschools.net>; Fazzino, Tabitha G. <TFazzino@dadeschools.net>; Pauline, Tiffanie A. <TPauline@dadeschools.net>; Santiestebanpardo, Vivian M. <VSpardo@dadeschools.net>; Steiger, Ron Y. <RSteiger@dadeschools.net>; Mantilla, Rene <RMantilla@dadeschools.net>
"""  # Replace this with your actual long string

# Regular expression to capture "First Last <email>" or just "email"
pattern = re.compile(r'(?:(?P<name>[^<>\n]+?)\s*)?<(?P<email>[^<>@\s]+@[^<>\s]+)>|(?P<lonely_email>[^<>\s;]+@[^\s;<>]+)')

results = []

for match in pattern.finditer(raw_data):
    if match.group("email"):
        email = match.group("email").strip()
        name = match.group("name")
        if name:
            name_parts = name.strip().replace('"', '').split()
            if len(name_parts) == 1:
                first_name = name_parts[0]
                last_name = ''
            else:
                first_name = name_parts[0]
                last_name = ' '.join(name_parts[1:])
        else:
            first_name = ''
            last_name = ''
    else:
        email = match.group("lonely_email").strip()
        first_name = ''
        last_name = ''

    results.append({
        'First Name': first_name,
        'Last Name': last_name,
        'Email': email
    })

# Write results to CSV
with open('contacts2.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['First Name', 'Last Name', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print("CSV file 'contacts2.csv' has been created.")
