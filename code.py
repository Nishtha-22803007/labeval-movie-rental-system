def rent_movie(listmovie,movies,item,name,id,trans,rent):
    if item not in listmovie:
        listmovie.append(item);
        movies[item]={'custname':name,'custid':id,'rentaltrans':trans,'rent':rent}
        print("Movie added")
    else:
        print("movie already rented")
def return_movie(listmovie,movies,item):
    if item in listmovie:
        listmovie.remove(item)
        print("movie returned successfully")
    else:
        print("movie was not rented")
def generate_report(listmovie,movies):
    print('current rented movies--')
    for i in listmovie:
        print(i,"->")
        print(movies[i])

  movies={'stree2':{
    'custname':'xyz',
    'custid':2,
    'rentaltrans':'cash',
    'rent':400
},'adinath':{
    'custname':'abc',
    'custid':3,
    'rentaltrans':'upi',
    'rent':600
}}
listmovie=['stree2','adinath']
print('Movie rental service')
while(True):
    print('\n\n1. Rent a movie\n2. Return a movie\n3. Generate rental report\n4. Exit\n\n')
    ch=int(input("enter choice:"))
    if ch==1:
        name=input("Enter movie name:")
        custname=input("enter customer name:")
        cusid=int(input("enter customer id:"))
        typetr=input("enter transaction type:")
        rent=int(input("enter value of rent:"))
        rent_movie(listmovie,movies,name,custname,cusid,typetr,rent)
    elif ch==2:
        name=input("Enter movie name to be returned:")
        return_movie(listmovie,movies,name)
    elif ch==3:
        generate_report(listmovie,movies)
    else:
        break
