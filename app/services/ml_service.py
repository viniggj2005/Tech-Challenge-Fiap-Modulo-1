from app.services.data_service import get_csv_data,get_db_data

availability={"In stock":0}
categories={'Travel':0, 'Mystery':1, 'Historical Fiction':2,'Sequential Art':3,'Classics':4,
 'Philosophy':5, 'Romance':6,'Womens Fiction':7, 'Fiction':8, 'Childrens':9, 'Religion':10,
 'Nonfiction':11, 'Music':12, 'Default':13, 'Science Fiction':14, 'Sports and Games':15,
 'Add a comment':16, 'Fantasy':17, 'New Adult':18, 'Young Adult':19, 'Science':20, 'Poetry':21,
 'Paranormal':22, 'Art':23, 'Psychology':24,'Autobiography':25, 'Parenting':26,
 'Adult Fiction':27, 'Humor':28, 'Horror':29, 'History':30, 'Food and Drink':31,
 'Christian Fiction':32, 'Business':33, 'Biography':34, 'Thriller':35, 'Contemporary':36,
 'Spirituality':37, 'Academic':38, 'Self Help':39, 'Historical':40, 'Christian':41, 'Suspense':42,
 'Short Stories':43, 'Novels':44, 'Health':45, 'Politics':46, 'Cultural':47, 'Erotica':48, 'Crime':49}
def get_data_for_features():
    # data=get_csv_data()
    data=get_db_data()
    data=data.drop(columns=["image","title","id"])
    # print(data["category"].unique())
    data["availability"] = data["availability"].map(availability)
    data["category"]=data["category"].map(categories)

    return{"features":data.to_dict(orient="records")}