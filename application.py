from cgi import print_arguments
from heapq import merge
from unittest import result
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def connect_firestore():
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase = firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

def add_data(db):

    title = input('\nEnter the title of the thing you want to add: ')
    creator = input('\nEnter the name of the person who made this (NA if so desired): ')
    rating = int(input('\nEnter your rating of this between 1 and 10: '))
    description = input('\nAdd a description (NA if so desired): ')

    data = {
        'title': f'{title}',
        'creator': f'{creator}',
        'rating': rating,
        'description': f'{description}'
    }

    db.collection('Library').document(f'{title}').set(data)

def remove_data(db):
    pass

def modify_data(db):
    pass

def view_data(db):

    print()
    docs = db.collection('Library').get()
    num = 0

    for doc in docs:
        num += 1
        docu = doc.to_dict()
        title = docu.get('title')

        print(f'{num}: {title}')

    choice = int(input('\nChoose the number of the thing you want to see: '))

    print()
    print(docs[choice - 1].to_dict())
    print()




def main():
    db = connect_firestore()

    ans = None

    while ans != '0':
        
        print()
        print('0: quit')
        print('1: add to liked things')        
        print('2: remove from liked things')
        print('3: modify liked things')
        print('4: view liked things')

        ans = input('\n>> ')
        
        if ans == '1':
            add_data(db)
        elif ans == '2':
            remove_data(db)
        elif ans == '3':
            modify_data(db)
        elif ans == '4':
            view_data(db)
        elif ans != '0':
            print('\nInvalid Input!')
        else:
            print('\n Goodbye')


    
    


if __name__ == '__main__':
    main()


# get document with known ID
# result = db.collection('Library').document('yes').get()
# if result.exists:
#     print(result.to_dict())

# get all documents in a collection
# docs = db.collection('Library').get()
#     for doc in docs:
#         print(doc.to_dict())

# querying
# docs = db.collection('Library').where('rating', '==', 5).get()
#     for doc in docs:
#         print(doc.to_dict())


# add document with Auto Id
# data = {
#     'name':'Jane',
#     'age':25, 
#     'employed':True,
#     'Hair_Color':'brown'
#     }
# db.collection('people').add(data)

# set documents with known ID
# data = {
#     'name':'Johnny',
#     'age':25, 
#     'employed':True,
#     'Hair_Color':'brown'
#     }
# db.collection('people').document('Johnny').set(data)

# add data without overwriting old data
# db.collection('people').document('Johnny').set({'address':'tokyo'}, merge=True)



