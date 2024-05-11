

#q9_3_1
def my_mp3_playlist(file_path):
    try:
        with open(file_path, 'r') as file:
            songs = file.read().split(';')
            songs = [song.strip() for song in songs if song.strip()]

            max_length = 0
            longest_song = ''
            performers = {}

            for i in range(0, len(songs), 3):
                song_name = songs[i]
                performer = songs[i + 1]
                length = songs[i + 2]

                minutes, seconds = map(int, length.split(':'))
                total_seconds = minutes * 60 + seconds
                if total_seconds > max_length:
                    max_length = total_seconds
                    longest_song = song_name

                performers[performer] = performers.get(performer, 0) + 1

            num_songs = len(songs) // 3
            most_common_performer = max(performers, key=performers.get)

            return (longest_song, num_songs, most_common_performer)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except (IndexError, ValueError):
        print("Invalid file format.")


#q9_3_2
def my_mp4_playlist(file_path, new_song):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        while len(lines) < 3:
            lines.append(';\n')

        song_data = lines[2].strip().split(';')
        song_data[0] = new_song
        lines[2] = ';'.join(song_data) + ';\n'

        with open(file_path, 'w') as file:
            file.writelines(lines)

        with open(file_path, 'r') as file:
            print(file.read())

    except FileNotFoundError:
        print(f"File {file_path} not found.")


if __name__ == '__main__':
    print(my_mp3_playlist("songs.txt"))

    my_mp4_playlist("songs.txt", "Python Love Story")