from urllib.request import urlopen

# import json
import json

# store the URL in url as
# parameter for urlopen
url = "https://petition.parliament.uk/petitions/700143.json"

# store the response of URL
global response
response = urlopen(url)
global data
data = json.loads(response.read())


def signatures_by_type(data_type):
    largest_sigs = data["data"]["attributes"][f"signatures_by_{data_type}"][0]["signature_count"]
    second_largest_sigs = data["data"]["attributes"][f"signatures_by_{data_type}"][1]["signature_count"]
    third_largest_sigs = data["data"]["attributes"][f"signatures_by_{data_type}"][2]["signature_count"]

    largest_name = data["data"]["attributes"][f"signatures_by_{data_type}"][0]["name"]
    second_largest_name = data["data"]["attributes"][f"signatures_by_{data_type}"][1]["name"]
    third_largest_name = data["data"]["attributes"][f"signatures_by_{data_type}"][2]["name"]

    for i in range(0, len(data["data"]["attributes"][f"signatures_by_{data_type}"])):
        no_sig = data["data"]["attributes"][f"signatures_by_{data_type}"][i]["signature_count"]
        if no_sig > largest_sigs:
            largest_sigs = no_sig
            largest_name = data["data"]["attributes"][f"signatures_by_{data_type}"][i]["name"]
        elif no_sig > second_largest_sigs:
            second_largest_sigs = no_sig
            second_largest_name = data["data"]["attributes"][f"signatures_by_{data_type}"][i]["name"]
        elif no_sig > third_largest_sigs:
            third_largest_sigs = no_sig
            third_largest_name = data["data"]["attributes"][f"signatures_by_{data_type}"][i]["name"]

    return (
    largest_name, largest_sigs, second_largest_name, second_largest_sigs, third_largest_name, third_largest_sigs)


def country_percentages():
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
    print("Country with the most signatures: ", signatures_by_type("country")[0], "with",
          signatures_by_type("country")[1], "signatures")
    print("Country with the second most signatures: ", signatures_by_type("country")[2], "with",
          signatures_by_type("country")[3], "signatures")
    print("Country with the third most signatures: ", signatures_by_type("country")[4], "with",
          signatures_by_type("country")[5], "signatures")
    print("Constituency with the most signatures: ", signatures_by_type("constituency")[0], "with",
          signatures_by_type("constituency")[1], "signatures")
    print("Constituency with the second most signatures: ", signatures_by_type("constituency")[2], "with",
          signatures_by_type("constituency")[3], "signatures")
    print("Constituency with the third most signatures: ", signatures_by_type("constituency")[4], "with",
          signatures_by_type("constituency")[5], "signatures")
    print("Region with the most signatures: ", signatures_by_type("region")[0], "with", signatures_by_type("region")[1],
          "signatures")
    print("Region with the second most signatures: ", signatures_by_type("region")[2], "with",
          signatures_by_type("region")[3], "signatures")
    print("Region with the third most signatures: ", signatures_by_type("region")[4], "with",
          signatures_by_type("region")[5], "signatures")


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
            largest_name, largest_sigs, second_largest_name, second_largest_sigs, third_largest_name, third_largest_sigs = signatures_by_type(
                "country")
            print(f"The country with the largest signatures is {largest_name} with {largest_sigs} signatures.")
            print(
                f"The country with the second largest signatures is {second_largest_name} with {second_largest_sigs} signatures.")
            print(
                f"The country with the third largest signatures is {third_largest_name} with {third_largest_sigs} signatures.")
        elif choice == 2:
            largest_name, largest_sigs, second_largest_name, second_largest_sigs, third_largest_name, third_largest_sigs = signatures_by_type(
                "constituency")
            print(f"The constituency with the largest signatures is {largest_name} with {largest_sigs} signatures.")
            print(
                f"The constituency with the second largest signatures is {second_largest_name} with {second_largest_sigs} signatures.")
            print(
                f"The constituency with the third largest signatures is {third_largest_name} with {third_largest_sigs} signatures.")
        elif choice == 3:
            largest_name, largest_sigs, second_largest_name, second_largest_sigs, third_largest_name, third_largest_sigs = signatures_by_type(
                "region")
            print(f"The region with the largest signatures is {largest_name} with {largest_sigs} signatures.")
            print(
                f"The region with the second largest signatures is {second_largest_name} with {second_largest_sigs} signatures.")
            print(
                f"The region with the third largest signatures is {third_largest_name} with {third_largest_sigs} signatures.")
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

