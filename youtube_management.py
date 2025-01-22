import sqlite3 as sq
conn=sq.connect('youtube_videos.db')
c=conn.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS yt(
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          time TEXT NOT NULL)
''' )

def list_videos():
    c.execute('SELECT * FROM yt ')
    fet=c.fetchall()
    if not fet:
        print("\n NO RECORD FOUND")
    else:
        for i in fet:
            print(f'\n RECORD :{i}')

def add_video(name,time):
    c.execute('INSERT INTO yt (name,time) VALUES(?,?)',(name,time))
    conn.commit()

def update_video(id,name,time):
    c.execute('UPDATE yt SET name=?, time=? WHERE rowid=? ',(name,time,id))
    conn.commit()

def delete_video(id):
    c.execute('DELETE FROM yt WHERE rowid=?',(id,))
    conn.commit()
 
def main():

    while True:
        print("\n Youtube manager app with db")
        print('1. List of Videos')
        print('2. ADD Videos')
        print('3. UPDATE Videos')
        print('4. DELETE Videos')
        print('5. EXIT')
        choice = input("Enter the No. of Desired action :")
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input('Enter the name of video here :')
            time = input('Enter the time of video :')
            add_video(name,time)
        elif choice == "3":
            id=input('Enter ID of the field :')
            new_name = input('Enter Name here :')
            new_time = input('Enter the time of the video :')
            update_video(id,new_name,new_time)
        elif choice == "4":
            row_id = input('Enter the id of the video :') 
            delete_video(row_id)
        elif choice == "5":
            break
        else:
            print('You have Entered as Invalid Choice')
            
    conn.close()

if __name__ == "__main__":
    main()
