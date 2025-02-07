from bs4 import BeautifulSoup
import requests
import csv

base_url1 = 'https://www.incomebyzipcode.com/search?utf8=%E2%9C%93&search%5Bterms%5D='
base_url2 = 'https://www.incomebyzipcode.com/'

# with open('zipcode.csv', newline='') as csvfile:
#     data = list(csv.reader(csvfile))

pincodes = ['11420', '10178', '11432', '10112', '10029', '10176', '11417', '10171', '10152', '10120', '10469', '10279', '10075', '10004', '11354', '11375', '10000', '11356', '10453', '11229', '10105', '10069', '11430', '10165', '10041', '11201', '10466', '10129', '0', '11422', '10007', '11214', '11362', '10175', '10037', '10013', '11691', '10038', '11377', '11366', '11228', '11379', '10001', '10452', '10005', '11434', '11360', '10467', '10167', '11234', '11004', '10472', '10312', '11694', '11697', '10026', '11205', '10303', '11239', '11361', '11215', '11040', '11412', '10123', '10022', '11216', '10002', '11359', '11427', '10048', '10454', '10458', '11419', '11372', '10018', '10451', '11416', '10177', '11224', '11374', '10151', '11435', '10456', '10460', '11209', '10032', '10119', '10314', '10305', '10473', '11237', '10461', '10271', '11103', '10106', '10020', '10103', '10111', '10080', '10030', '10010', '11213', '11207', '10031', '10170', '10162', '11211', '11203', '11369', '11413', '11367', '10128', '11365', '11235', '10025',
            '11421', '11208', '11426', '11378', '10457', '11368', '10281', '11428', '10006', '10464', '11233', '11106', '10471', '11222', '10033', '11423', '10155', '10468', '10024', '10307', '11101', '10017', '11232', '10301', '10110', '10040', '10455', '11038', '10034', '11373', '11220', '10153', '11355', '10065', '10306', '10121', '11429', '10016', '10462', '11210', '10097', '11219', '11226', '11218', '10459', '11104', '11364', '11385', '10474', '10028', '10302', '10174', '10465', '11370', '11241', '11221', '11363', '11695', '10009', '10158', '10012', '11001', '11206', '10014', '11418', '10308', 'N/A', '10036', '10035', '11357', '10021', '11411', '11433', '11212', '10019', '11249', '00083', '10173', '10118', '10023', '10011', '11251', '10475', '10115', '11436', '11415', '11231', '10154', '10470', '10282', '11225', '11204', '10027', '11358', '10044', '10304', '11109', '10039', '10309', '11230', '11693', '11414', '10003', '11692', '10172', '11223', '10278', '10280', '11236', '10463', '11217', '10310', '10045', '11102', '11238', '11105']

session = requests.Session()

with open('zip-income-data.csv', 'w') as file:
    writer = csv.writer(file) 

    for pincode in pincodes:
        data = [pincode]

        soup = BeautifulSoup(session.get(base_url1 + pincode).content, 'html.parser')
        try: # if the zipcode obtained from film-permits is corrupt or doesn't exist.
        	ref = soup.find('td').a['href']
        	soup = BeautifulSoup(session.get(base_url2 + ref).content, 'html.parser')

	        for el in soup.find_all(class_ = "hilite")[:4]:
	            data += el.contents

	        writer.writerow(data)
        except:
            print("Skipped ZipCode {}".format(pincode))
            continue



		
      
