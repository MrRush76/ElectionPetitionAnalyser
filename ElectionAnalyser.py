import json

def country_signatures():
    with open('700143.json') as f:
        data = json.load(f)
    largest_sigs = data["data"]["attributes"]["signatures_by_country"][0]["signature_count"]
    second_largest_sigs = data["data"]["attributes"]["signatures_by_country"][1]["signature_count"]
    third_largest_sigs = data["data"]["attributes"]["signatures_by_country"][2]["signature_count"]

    largest_country = data["data"]["attributes"]["signatures_by_country"][0]["name"]
    second_largest_country = data["data"]["attributes"]["signatures_by_country"][1]["name"]
    third_largest_country = data["data"]["attributes"]["signatures_by_country"][2]["name"]

    for i in range(0, len(data["data"]["attributes"]["signatures_by_country"])):
        no_sig = data["data"]["attributes"]["signatures_by_country"][i]["signature_count"]
        if no_sig > largest_sigs:
            largest_sigs = no_sig
            largest_country = data["data"]["attributes"]["signatures_by_country"][i]["name"]
        elif no_sig > second_largest_sigs:
            second_largest_sigs = no_sig
            second_largest_country = data["data"]["attributes"]["signatures_by_country"][i]["name"]
        elif no_sig > third_largest_sigs:
            third_largest_sigs = no_sig
            third_largest_country = data["data"]["attributes"]["signatures_by_country"][i]["name"]

    return (largest_country, largest_sigs, second_largest_country, second_largest_sigs, third_largest_country, third_largest_sigs)

def constituency_signatures():
    with open('700143.json') as f:
        data = json.load(f)
    largest_sigs = data["data"]["attributes"]["signatures_by_constituency"][0]["signature_count"]
    second_largest_sigs = data["data"]["attributes"]["signatures_by_constituency"][1]["signature_count"]
    third_largest_sigs = data["data"]["attributes"]["signatures_by_constituency"][2]["signature_count"]

    largest_constituency = data["data"]["attributes"]["signatures_by_constituency"][0]["name"]
    second_largest_constituency = data["data"]["attributes"]["signatures_by_constituency"][1]["name"]
    third_largest_constituency = data["data"]["attributes"]["signatures_by_constituency"][2]["name"]

    for i in range(0, len(data["data"]["attributes"]["signatures_by_constituency"])):
        no_sig = data["data"]["attributes"]["signatures_by_constituency"][i]["signature_count"]
        if no_sig > largest_sigs:
            largest_sigs = no_sig
            largest_constituency = data["data"]["attributes"]["signatures_by_constituency"][i]["name"]
        elif no_sig > second_largest_sigs:
            second_largest_sigs = no_sig
            second_largest_constituency = data["data"]["attributes"]["signatures_by_constituency"][i]["name"]
        elif no_sig > third_largest_sigs:
            third_largest_sigs = no_sig
            third_largest_constituency = data["data"]["attributes"]["signatures_by_constituency"][i]["name"]

    return (largest_constituency, largest_sigs, second_largest_constituency, second_largest_sigs, third_largest_constituency, third_largest_sigs)

def region_signatures():
    with open('700143.json') as f:
        data = json.load(f)
    largest_sigs = data["data"]["attributes"]["signatures_by_region"][0]["signature_count"]
    second_largest_sigs = data["data"]["attributes"]["signatures_by_region"][1]["signature_count"]
    third_largest_sigs = data["data"]["attributes"]["signatures_by_region"][2]["signature_count"]

    largest_region = data["data"]["attributes"]["signatures_by_region"][0]["name"]
    second_largest_region = data["data"]["attributes"]["signatures_by_region"][1]["name"]
    third_largest_region = data["data"]["attributes"]["signatures_by_region"][2]["name"]

    for i in range(0, len(data["data"]["attributes"]["signatures_by_region"])):
        no_sig = data["data"]["attributes"]["signatures_by_region"][i]["signature_count"]
        if no_sig > largest_sigs:
            largest_sigs = no_sig
            largest_region = data["data"]["attributes"]["signatures_by_region"][i]["name"]
        elif no_sig > second_largest_sigs:
            second_largest_sigs = no_sig
            second_largest_region = data["data"]["attributes"]["signatures_by_region"][i]["name"]
        elif no_sig > third_largest_sigs:
            third_largest_sigs = no_sig
            third_largest_region = data["data"]["attributes"]["signatures_by_region"][i]["name"]

    return (largest_region, largest_sigs, second_largest_region, second_largest_sigs, third_largest_region, third_largest_sigs)

def country_percentages():
    with open('700143.json') as f:
        data = json.load(f)
    total_sigs = data["data"]["attributes"]["signature_count"]
    percentages = []
    for i in range(0, len(data["data"]["attributes"]["signatures_by_country"])):
        no_sig = data["data"]["attributes"]["signatures_by_country"][i]["signature_count"]
        percentage = (no_sig / total_sigs) * 100
        percentages.append((data['data']['attributes']['signatures_by_country'][i]['name'], percentage))
    out_of_uk_percentage = 0
    for i in range(0, len(percentages)):
        if percentages[i][0] != "United Kingdom":
            out_of_uk_percentage += percentages[i][1]
    out_of_uk_votes = 0
    for i in range(0, len(data["data"]["attributes"]["signatures_by_country"])):
        if data["data"]["attributes"]["signatures_by_country"][i]["name"] != "United Kingdom":
            out_of_uk_votes += data["data"]["attributes"]["signatures_by_country"][i]["signature_count"]
    return percentages, out_of_uk_votes, out_of_uk_percentage


def full_breakdown():
    print("Country with the most signatures: ", country_signatures()[0], "with", country_signatures()[1], "signatures")
    print("Country with the second most signatures: ", country_signatures()[2], "with", country_signatures()[3], "signatures")
    print("Country with the third most signatures: ", country_signatures()[4], "with", country_signatures()[5], "signatures")
    print("Constituency with the most signatures: ", constituency_signatures()[0], "with", constituency_signatures()[1], "signatures")
    print("Constituency with the second most signatures: ", constituency_signatures()[2], "with", constituency_signatures()[3], "signatures")
    print("Constituency with the third most signatures: ", constituency_signatures()[4], "with", constituency_signatures()[5], "signatures")
    print("Region with the most signatures: ", region_signatures()[0], "with", region_signatures()[1], "signatures")
    print("Region with the second most signatures: ", region_signatures()[2], "with", region_signatures()[3], "signatures")
    print("Region with the third most signatures: ", region_signatures()[4], "with", region_signatures()[5], "signatures")
    print("Percentage of votes from outside the uk: ", country_percentages()[2])
    print("Percentage of votes from  the UK: ", 100 - country_percentages()[2])
    print("Votes from outside the UK: ", country_percentages()[1])


def menu():
    while True:
        print("1. Country Signatures")
        print("2. Constituency Signatures")
        print("3. Region Signatures")
        print("4. Country Percentages")
        print("5. Full Breakdown")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            largest_country, largest_sigs, second_largest_country, second_largest_sigs, third_largest_country, third_largest_sigs = country_signatures()
            print(f"The country with the largest signatures is {largest_country} with {largest_sigs} signatures.")
            print(f"The country with the second largest signatures is {second_largest_country} with {second_largest_sigs} signatures.")
            print(f"The country with the third largest signatures is {third_largest_country} with {third_largest_sigs} signatures.")
        elif choice == 2:
            largest_constituency, largest_sigs, second_largest_constituency, second_largest_sigs, third_largest_constituency, third_largest_sigs = constituency_signatures()
            print(f"The constituency with the largest signatures is {largest_constituency} with {largest_sigs} signatures.")
            print(f"The constituency with the second largest signatures is {second_largest_constituency} with {second_largest_sigs} signatures.")
            print(f"The constituency with the third largest signatures is {third_largest_constituency} with {third_largest_sigs} signatures.")
        elif choice == 3:
            largest_region, largest_sigs, second_largest_region, second_largest_sigs, third_largest_region, third_largest_sigs = region_signatures()
            print(f"The region with the largest signatures is {largest_region} with {largest_sigs} signatures.")
            print(f"The region with the second largest signatures is {second_largest_region} with {second_largest_sigs} signatures.")
            print(f"The region with the third largest signatures is {third_largest_region} with {third_largest_sigs} signatures.")
        elif choice == 4:
            percentages, out_of_uk_votes, out_of_uk_percentages = country_percentages()
            for country, percentage in percentages:
                print(f"{country} has {percentage:.4f}% of the signatures.")
            print(f"{out_of_uk_votes} votes are from outside the UK.")
            print(f"{out_of_uk_percentages:.4f}% of the votes are from outside the UK.")
        elif choice == 5:
            full_breakdown()
        elif choice == 6:
            exit()
        else:
            print("Invalid choice")

menu()
