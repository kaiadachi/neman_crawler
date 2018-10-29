import csv
import codecs

def amazon_fa(name):
    list = []
    with codecs.open('gui_src/amazon_fasion.csv', "r", "Shift-JIS", "ignore") as f:
        reader = csv.reader(f)
        for row in reader:
            list.append(row)

    num = []
    for i in range(3):
        num.append(list[i])

    with codecs.open('../created_csv/amazon_fashion_{0}'.format(name),'w', "Shift-JIS", "ignore") as b:
        writer = csv.writer(b,lineterminator='\n')
        writer.writerows(num)

        with codecs.open('../nm_origin_csv/{0}'.format(name),"r", "Shift-JIS", "ignore") as f:
            reader = csv.reader(f)
            header = next(reader)

            first = 1
            for row in reader:
                if (row[5] != ""):
                    row[4] = row[5]
                if(first == 1):
                    title = row[1]
                    first = 0
                    parent = [row[3],row[1],"","",row[2],"",row[3],"","",row[3],"",
                         "18","新品","","","","","","","exclude cod","","",
                         "","","","","","","","","","JP Parallel Import","","","",
                         "当商品はお届けまで２から３週間ほどお時間をいただいております。 アメリカ正規品取扱店からの並行輸入商品となります。",
                         "返品、交換につきましては当社規定のポリシーがありますので当社ページのヘルプから事前にご確認下さい。ご注文頂いた場合注意事項をご了承いただいたものと致します。",
                         "商品の発送は、日本国内発送またはアメリカからの直送となります。どちらの場合でも必ず追跡番号がある発送方法でお届けいたします。",
                         "在庫状況は常に変動しています。また、ご注文後に在庫が確保できない場合もございますので、何卒ご了承ください。",
                         "","","2221135051","スポーティー","",row[10],"",row[11],row[12],row[13],row[14],row[15],
                         "","","","","","","","","","","Parent","","","Size","" + "",
                         "","","","","","","","","","","","","","","","","",row[9],
                         "","","","","","","","","","","","","","","","","",""
                         ]
                    writer.writerow(parent)

                if(title == row[1]):
                    s = [row[3] + row[7] + row[6],row[1],"","",row[2],"",row[3],"","",row[3] + row[7] + row[6],row[8],
                         "18","新品","",row[4],"","","","","exclude cod","","",
                         "","","","","","","","","","JP Parallel Import","","","",
                         "当商品はお届けまで２から３週間ほどお時間をいただいております。 アメリカ正規品取扱店からの並行輸入商品となります。",
                         "返品、交換につきましては当社規定のポリシーがありますので当社ページのヘルプから事前にご確認下さい。ご注文頂いた場合注意事項をご了承いただいたものと致します。",
                         "商品の発送は、日本国内発送またはアメリカからの直送となります。どちらの場合でも必ず追跡番号がある発送方法でお届けいたします。",
                         "在庫状況は常に変動しています。また、ご注文後に在庫が確保できない場合もございますので、何卒ご了承ください。",
                         "","","2221135051","スポーティー","",row[10],"",row[11],row[12],row[13],row[14],row[15],
                         "","","","","","","","","","","Child",row[3],"Variation","Size","サイズ" + row[6],
                         row[6],row[7],row[7],"","","","","","","","","","","","","","",row[9],
                         "","","","","","","","","","","","","","","","","",""
                         ]

                    writer.writerow(s)

                else:
                    parent = [row[3],row[1],"","",row[2],"",row[3],"","",row[3],"",
                         "18","新品","","","","","","","exclude cod","","",
                         "","","","","","","","","","JP Parallel Import","","","",
                         "当商品はお届けまで２から３週間ほどお時間をいただいております。 アメリカ正規品取扱店からの並行輸入商品となります。",
                         "返品、交換につきましては当社規定のポリシーがありますので当社ページのヘルプから事前にご確認下さい。ご注文頂いた場合注意事項をご了承いただいたものと致します。",
                         "商品の発送は、日本国内発送またはアメリカからの直送となります。どちらの場合でも必ず追跡番号がある発送方法でお届けいたします。",
                         "在庫状況は常に変動しています。また、ご注文後に在庫が確保できない場合もございますので、何卒ご了承ください。",
                         "","","2221135051","スポーティー","",row[10],"",row[11],row[12],row[13],row[14],row[15],
                         "","","","","","","","","","","Parent","","","Size","" + "",
                         "","","","","","","","","","","","","","","","","",row[9],
                         "","","","","","","","","","","","","","","","","",""
                         ]
                    s = [row[3] + row[7] + row[6],row[1],"","",row[2],"",row[3],"","",row[3] + row[7] + row[6],row[8],
                         "18","新品","",row[4],"","","","","exclude cod","","",
                         "","","","","","","","","","JP Parallel Import","","","",
                         "当商品はお届けまで２から３週間ほどお時間をいただいております。 アメリカ正規品取扱店からの並行輸入商品となります。",
                         "返品、交換につきましては当社規定のポリシーがありますので当社ページのヘルプから事前にご確認下さい。ご注文頂いた場合注意事項をご了承いただいたものと致します。",
                         "商品の発送は、日本国内発送またはアメリカからの直送となります。どちらの場合でも必ず追跡番号がある発送方法でお届けいたします。",
                         "在庫状況は常に変動しています。また、ご注文後に在庫が確保できない場合もございますので、何卒ご了承ください。",
                         "","","2221135051","スポーティー","",row[10],"",row[11],row[12],row[13],row[14],row[15],
                         "","","","","","","","","","","Child",row[3],"Variation","Size","サイズ" + row[6],
                         row[6],row[7],row[7],"","","","","","","","","","","","","","",row[9],
                         "","","","","","","","","","","","","","","","","",""
                         ]
                    writer.writerow(parent)
                    writer.writerow(s)
                    title = row[1]
def amazon_out(name):
    list = []
    with codecs.open('gui_src/amazon_outdoor.csv',"r", "Shift-JIS", "ignore") as f:
        reader = csv.reader(f)
        for row in reader:
            list.append(row)

    num = []
    for i in range(3):
        num.append(list[i])

    with codecs.open('../created_csv/amazon_outdoor_{0}'.format(name),'w', "Shift-JIS", "ignore") as b:
        writer = csv.writer(b,lineterminator='\n')
        writer.writerows(num)

        with codecs.open('../nm_origin_csv/{0}'.format(name),"r", "Shift-JIS", "ignore") as f:
            reader = csv.reader(f)
            header = next(reader)

            first = 1
            for row in reader:
                if (row[5] != ""):
                    row[4] = row[5]
                if(first == 1):
                    title = row[1]
                    first = 0
                    parent = [row[3],"","",row[1],"",row[2],row[3],"",row[2],"","",
                             "","新品","","","","","","","18","exclude cod","",
                             "","","","","","","","","","JP Parallel Import","","","","","","","","","","","","","","",
                             "※※１枚目の画像が対象商品の色となります。２枚目以降の画像は色の違う場合もございますが、商品のイメージとして参考にしてください。※※",
                             "当商品はお届けまで２から３週間ほどお時間をいただいております。 アメリカ正規品取扱店からの並行輸入商品となります。",
                             "返品、交換につきましては当社規定のポリシーがありますので当社ページのヘルプから事前にご確認下さい。ご注文頂いた場合注意事項をご了承いただいたものと致します。",
                             "商品の発送は、日本国内発送またはアメリカからの直送となります。どちらの場合でも必ず追跡番号がある発送方法でお届けいたします。",
                             "在庫状況は常に変動しています。また、ご注文後に在庫が確保できない場合もございますので、何卒ご了承ください。",
                             "2131627051","","メンズ","レディース","",row[9],row[10],"",row[11],row[12],row[13],row[14],row[15],
                             "","","","","","","","","","","Parent","","","ColorSize","","","","","",
                             "","","","","","","","","","","","","","","","","",""
                             "","","","","","","","","","","","","","","","","","","","","",
                             ]
                    writer.writerow(parent)

                if(title == row[1]):
                    s = [row[3] + row[7] + row[6],"","",row[1],"",row[2],row[3],"",row[2],"",row[4],
                             "","新品","",row[8],"","","","","18","exclude cod","",
                             "","","","","","","","","","JP Parallel Import","","","","","","","","","","","","","","",
                             "※※１枚目の画像が対象商品の色となります。２枚目以降の画像は色の違う場合もございますが、商品のイメージとして参考にしてください。※※",
                             "当商品はお届けまで２から３週間ほどお時間をいただいております。 アメリカ正規品取扱店からの並行輸入商品となります。",
                             "返品、交換につきましては当社規定のポリシーがありますので当社ページのヘルプから事前にご確認下さい。ご注文頂いた場合注意事項をご了承いただいたものと致します。",
                             "商品の発送は、日本国内発送またはアメリカからの直送となります。どちらの場合でも必ず追跡番号がある発送方法でお届けいたします。",
                             "在庫状況は常に変動しています。また、ご注文後に在庫が確保できない場合もございますので、何卒ご了承ください。",
                             "2131627051","","メンズ","レディース","",row[9],row[10],"",row[11],row[12],row[13],row[14],row[15],
                             "","","","","","","","","","","Child",row[3],"Variation","ColorSize","","","","","",
                             row[7],row[7],"","","",row[6],"","","","","","","","","","","",""
                             "","","","","","","","","","","","","","","","","","","","","",
                             ]
                    writer.writerow(s)

                else:
                    parent = [row[3],"","",row[1],"",row[2],row[3],"",row[2],"","",
                             "","新品","","","","","","","18","exclude cod","",
                             "","","","","","","","","","JP Parallel Import","","","","","","","","","","","","","","",
                             "※※１枚目の画像が対象商品の色となります。２枚目以降の画像は色の違う場合もございますが、商品のイメージとして参考にしてください。※※",
                             "当商品はお届けまで２から３週間ほどお時間をいただいております。 アメリカ正規品取扱店からの並行輸入商品となります。",
                             "返品、交換につきましては当社規定のポリシーがありますので当社ページのヘルプから事前にご確認下さい。ご注文頂いた場合注意事項をご了承いただいたものと致します。",
                             "商品の発送は、日本国内発送またはアメリカからの直送となります。どちらの場合でも必ず追跡番号がある発送方法でお届けいたします。",
                             "在庫状況は常に変動しています。また、ご注文後に在庫が確保できない場合もございますので、何卒ご了承ください。",
                             "2131627051","","メンズ","レディース","",row[9],row[10],"",row[11],row[12],row[13],row[14],row[15],
                             "","","","","","","","","","","Parent","","","ColorSize","","","","","",
                             "","","","","","","","","","","","","","","","","",""
                             "","","","","","","","","","","","","","","","","","","","","",
                             ]
                    s = [row[3] + row[7] + row[6],"","",row[1],"",row[2],row[3],"",row[2],"",row[4],
                             "","新品","",row[8],"","","","","18","exclude cod","",
                             "","","","","","","","","","JP Parallel Import","","","","","","","","","","","","","","",
                             "※※１枚目の画像が対象商品の色となります。２枚目以降の画像は色の違う場合もございますが、商品のイメージとして参考にしてください。※※",
                             "当商品はお届けまで２から３週間ほどお時間をいただいております。 アメリカ正規品取扱店からの並行輸入商品となります。",
                             "返品、交換につきましては当社規定のポリシーがありますので当社ページのヘルプから事前にご確認下さい。ご注文頂いた場合注意事項をご了承いただいたものと致します。",
                             "商品の発送は、日本国内発送またはアメリカからの直送となります。どちらの場合でも必ず追跡番号がある発送方法でお届けいたします。",
                             "在庫状況は常に変動しています。また、ご注文後に在庫が確保できない場合もございますので、何卒ご了承ください。",
                             "2131627051","","メンズ","レディース","",row[9],row[10],"",row[11],row[12],row[13],row[14],row[15],
                             "","","","","","","","","","","Child",row[3],"Variation","ColorSize","","","","","",
                             row[7],row[7],"","","",row[6],"","","","","","","","","","","",""
                             "","","","","","","","","","","","","","","","","","","","","",
                         ]

                    writer.writerow(parent)
                    writer.writerow(s)
                    title = row[1]


def our_clo(name):
    with codecs.open('../created_csv/our_clothes_{0}'.format(name),'w',"Shift-JIS","ignore") as b:
        writer = csv.writer(b,lineterminator='\n')
        head = ["Handle","Title","Body (HTML)","Vendor","Type","Tags","Published","Option1 Name",
                "Option1 Value","Option2 Name","Option2 Value","Option3 Name","Option3 Value","Variant SKU",
                "Variant Grams","Variant Inventory Tracker","Variant Inventory Qty","Variant Inventory Policy",
                "Variant Fulfillment Service","Variant Price","Variant Compare At Price","Variant Requires Shipping",
                "Variant Taxable","Variant Barcode","Image Src"]
        writer.writerow(head)

        with codecs.open('../nm_origin_csv/{0}'.format(name),'r',"Shift-JIS","ignore") as f:
            reader = csv.reader(f)
            header = next(reader)
            first = 1
            for row in reader:

                if(first == 1):
                    title = row[1]
                    handle = row[3]
                    first = 0
                    countUrl = 0


                if(title == row[1]):
                    pass
                else:
                    if(countUrl < len(url)):
                        for i in range(countUrl, len(url)):
                            s = [ handle, "", "","","","","","","","","","","","","","","","","","","","","","",str(url[i]) ]
                            writer.writerow(s)
                            #print(", "+ title + ", , , , , , , , , , , , , , , , , , , , , , , " + str(url[i]))


                    title = row[1]
                    handle = row[3]
                    countUrl = 0

                url =[]
                for i in range(5):
                    if( str(row[10+i]) == "" ):
                        pass
                    else:
                        url.append(row[10+i])


                s = []
                #Handle
                s.append(str(row[3]))
                #Title
                s.append(str(row[1]))
                #Body
                s.append("")
                #Vendor
                s.append("")
                #Type
                s.append("")
                #Tag
                s.append("")
                #Published
                s.append("TRUE")
                #Option1 Name
                s.append("size")
                #Option1 Value
                s.append(str(row[6]))
                #Option2 Name
                s.append("color")
                #Option2 Value
                s.append(str(row[7]))
                #Option3 Name
                s.append("")
                #Option3 Value
                s.append("")
                #Variant SKU
                s.append(row[3] + row[7] + row[6])
                #Variant Grams
                s.append("1000")
                #Variant Inventory Tracker
                s.append("")
                #Variant Inventory Qty
                s.append("1")
                #Variant Inventory Policy
                s.append("deny")
                #Variant Fulfillment Service
                s.append("manual")
                #Variant Price
                s.append(str(row[4]))
                #Variant Compare At Price
                s.append("")
                #Variant Requires Shipping
                s.append("TRUE")
                #Variant Taxable
                s.append("FALSE")
                #Variant Barcode
                s.append("")
                #Image Src
                if(countUrl < len(url)):
                    s.append(str(url[countUrl]))
                    countUrl = countUrl + 1

                writer.writerow(s)

def wow_item(name):
    with codecs.open('../created_csv/wowma_item_{0}'.format(name), 'w', "Shift-JIS", "ignore") as b:
        writer = csv.writer(b,lineterminator='\n')
        head = ["ctrlCol","lotNumber","itemCode","itemName","itemManagementId","itemManagementName","itemPrice","taxSegment","postageSegment","postage","deliveryId","deliveryMethodId1","deliveryMethodId2","deliveryMethodId3","deliveryMethodId4","deliveryMethodId5","deliveryMethodName1","deliveryMethodName2","deliveryMethodName3","deliveryMethodName4","deliveryMethodName5","publicStartDate","stockSegment",
                "choicesStockHorizontalItemName","choicesStockVerticalItemName","choicesStockUpperDescription","choicesStockLowerDescription","displayStockSegment","displayStockThreshold","displayChoicesStockThreshold","limitedOrderSegment","limitedOrderCount","stockCount","displayBackorderMessage","displayChoicesStockSegment","description","descriptionForSP","descriptionForPC","detailTitle","detailDescription",
                "specTitle","spec1","spec2","spec3","spec4","spec5","searchKeyword1","searchKeyword2","searchKeyword3","imageUrl1","imageUrl2","imageUrl3","imageUrl4","imageUrl5","imageUrl6","imageUrl7","imageUrl8","imageUrl9","imageUrl10",
                "imageName1","imageName2","imageName3","imageName4","imageName5","imageName6","imageName7","imageName8","imageName9","imageName10","pointRate","categoryId","tagId","jan","isbn","itemModel","limitedPasswd","limitedPasswdPageTitle","limitedPasswdPageMessage","saleStatus","itemOption1","itemOption2","itemOption3","itemOption4","itemOption5"]
        writer.writerow(head)
        with codecs.open('../nm_origin_csv/{0}'.format(name),"r", "Shift-JIS", "ignore") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:

                s = ["U","",row[3],row[1],row[3],"",row[4],"1","2","","","","","","","","","","","","","",
                     "2","","サイズ","商品サイズ","×在庫なし","","","","2","1","","再入荷お待ちください","1",
                     "発送について<br>〇発送前に商品の状態を確認いたします。靴箱や袋に潰れなどのダメージがあっても、商品に問題がないと判断した場合は、簡単な修繕をして発送いたしますのでご了承ください。<br>〇商品の発送は、日本国内発送またはアメリカからの直送となります。どちらの場合でも必ず追跡番号がある発送方法でお届けいたします。<br><br>在庫について<br>〇在庫状況は常に変動しています。ご希望サイズの在庫がない場合でも、お問い合わせいただけましたら、最新の在庫状況をお調べいたしますので、ご遠慮なくご連絡ください。また、ご注文後に在庫が確保できない場合もございますので、何卒ご了承ください。",
                     "当商品はアメリカ正規品取扱業者からの並行輸入商品です。お取り寄せのため、お届けまで２～３週間ほどお時間をいただいております。<br><br><div><a href=\"/user/38725928\"><img src=\"http://sukai9682.jp/test/product_page_banner.jpg\"></a></div>",
                     "当商品はアメリカ正規品取扱業者からの並行輸入商品です。お取り寄せのため、お届けまで２～３週間ほどお時間をいただいております。<br><br><div><a href=\"/user/38725928\"><img src=\"http://sukai9682.jp/test/product_page_banner.jpg\"></a></div>",
                     "商品詳細説明タイトル","商品詳細説明","","","","","","","新品","","ブランド",row[10],row[11],row[12],row[13],row[14],row[15],"","","","",
                     "メイン画像","サブ画像","サブ画像","サブ画像","サブ画像","サブ画像","","","","","","40520807","","","",row[3],"","","","1","","","","",""
                    ]
                writer.writerow(s)



def wow_stock(name):
    with codecs.open('../created_csv/wowma_stock_{0}'.format(name), 'w', "Shift-JIS", "ignore") as b:
        writer = csv.writer(b,lineterminator='\n')
        head = ["ctrlCol","lotNumber","itemCode","stockSegment","stockCount","choicesStockHorizontalName","choicesStockHorizontalCode","choicesStockHorizontalSeq","choicesStockVerticalName","choicesStockVerticalCode","choicesStockVerticalSeq","choicesStockCount","choicesStockShippingDayId","choicesStockShippingDayDispTxt"]
        writer.writerow(head)
        with codecs.open('../nm_origin_csv/{0}'.format(name),"r", "Shift-JIS", "ignore") as f:
            reader = csv.reader(f)
            header = next(reader)

            first = 1
            count = 0
            for row in reader:
                if(first == 1):
                    title = row[1]
                    first = 0
                if(title == row[1]):
                    count = count + 1
                    s = ["U","",row[3],"2","",row[7],row[7],"",row[6],row[6],count,row[8],"",""]
                    writer.writerow(s)

                else:
                    count = 0
                    count = count + 1
                    s = ["U","",row[3],"2","",row[7],row[7],"",row[6],row[6],count,row[8],"",""]
                    writer.writerow(s)
                    title = row[1]
