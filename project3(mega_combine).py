# code by sarvesh@2004
import tkinter as tk  
import cv2
import subprocess
import pyttsx3
from tkinter import filedialog
import PyPDF2
root = tk.Tk()
root.withdraw()
engine=pyttsx3.init()

#if after selecting or saving file gives error then give the path of specific file in this code . 
# like pdf or img = "location of file you want select like ->"path/image.jpg" or "path/pdf1.pdf" " 
# choose no. what you want to do sarvesh !..
a = int(input("choose no. what you want to do : 1-> image resizer  2-> image resizer with robo speaker  3-> pdf merge  4->pdf merge with robo speaker  5->file convertor  6->file convertor with robo speaker  7-> split pdf  8-> split pdf according to page no. you want  9->extract text from pdf  10-> extract text from pdf with page no. you want :  "))
match a:
    case 1 :
        print("select you img from your directory")
        img = filedialog.askopenfilenames()
        scale_percent = int(input("Enter the percentage of the new img you want and select only img files :"))
        src = cv2.imread(img,cv2.IMREAD_UNCHANGED)
        new_width = int(src.shape[1]*scale_percent/100)
        new_height = int(src.shape[0]*scale_percent/100)
        ouput = cv2.resize(src, (new_width,new_height))
        new_img = filedialog.asksaveasfilename()
        cv2.imwrite(new_img,ouput)
        

    case 2 :
        engine.say("select you img from your directory")
        print("select you img from your directory")
        engine.runAndWait()
        engine.say("select your file ")
        engine.runAndWait()
        img = filedialog.askopenfilenames()
        engine.say("Enter the percentage of the new img you want and select only img files")
        engine.runAndWait()
        scale_percent = int(input("Enter the percentage of the new img you want and select only img files :"))
        src = cv2.imread(img,cv2.IMREAD_UNCHANGED)
        new_width = int(src.shape[1]*scale_percent/100)
        new_height = int(src.shape[0]*scale_percent/100)
        ouput = cv2.resize(src, (new_width,new_height))
        new_img = filedialog.asksaveasfilename()
        engine.say("finally file is ready")
        engine.runAndWait()
        cv2.imwrite(new_img,ouput)
        engine.stop()
        

    case 3 :
        pdfmerger = PyPDF2.PdfMerger()
        # select pdf1 from directory
        pdf1 = filedialog.askopenfilename() 

            # select pdf2 from directory
        pdf2 = filedialog.askopenfilename()

        # appending those selected pdf
        pdfmerger.append(pdf1)
        pdfmerger.append(pdf2)

        # give the name of output of merged selected pdfs
        output = filedialog.asksaveasfilename()
        pdfmerger.write(output)
        pdfmerger.close()
        
    
    case 4 :
        pdfmerger = PyPDF2.PdfMerger()
        # select pdf1 from directory
        engine.say("select your fist file")
        engine.runAndWait()
        pdf1 = filedialog.askopenfilename() 

        # select pdf2 from directory
        engine.say("select your second file")
        engine.runAndWait()
        pdf2 = filedialog.askopenfilename()

        # appending those selected pdf
        pdfmerger.append(pdf1)
        pdfmerger.append(pdf2)

        # give the name of output of merged selected pdfs
        engine.say("finally file is ready")
        engine.runAndWait()
        output = filedialog.asksaveasfilename()
        pdfmerger.write(output)
        pdfmerger.close()
        engine.stop()
       
    
    case 5 :
        input_file = filedialog.askopenfilenames()
        output_format = input("enter yout file format you want in ouput : ")
        output_file = filedialog.asksaveasfilename()
        command = ["libreoffice", "--headless", "--convert-to", output_format, input_file, "--outdir", output_file]
        subprocess.call(command)
        
    
    case 6 :
        engine.say("select your first file ")
        engine.runAndWait()
        input_file = filedialog.askopenfilenames()
        engine.say("enter yout file format you want in ouput")
        engine.runAndWait()
        output_format = input("enter yout file format you want in ouput : ")
        engine.say("select your second file")
        engine.runAndWait()
        output_file = filedialog.asksaveasfilename()
        command = ["libreoffice", "--headless", "--convert-to", output_format, input_file, "--outdir", output_file]
        subprocess.call(command)
        engine.stop()
        
    
    # split of pdf
    case 7 :
        pdf1 = filedialog.askopenfilenames()
        pdf_file = open(pdf1, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        new_pdf_file_1 = open('my_pdf_file_pages_1_10.pdf', 'wb')
        
        for page_num in range(10):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
            pdf_writer.write(new_pdf_file_1)
            new_pdf_file_1.close()
            new_pdf_file_2 = open('my_pdf_file_pages_11_end.pdf', 'wb')

        for page_num in range(10, pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
            pdf_writer.write(new_pdf_file_2)
            new_pdf_file_2.close()
        pdf_file.close()
    
    # split of pdf according to no. of pages wants 
    case 8:  
        pdf1 = filedialog.askopenfilenames()
        pdf_file = open(pdf1, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            new_pdf_file = open('my_pdf_file_page_{}.pdf'.format(page_num + 1), 'wb')
            pdf_writer.addPage(pdf_reader.getPage(page_num))
            pdf_writer.write(new_pdf_file)
            new_pdf_file.close()
        pdf_file.close()
        

    case 9:
        pdf1 = filedialog.askopenfilenames()
        pdf_file = open(pdf1, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        page = pdf_reader.getPage(0)
        text = page.extractText()
        pdf_file.close()
        print(text)
        
    
    case 10:
        pdf1 = filedialog.askopenfilenames()
        pdf_file = open(pdf1, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages
        text = ''
        for i in range(num_pages):
            page = pdf_reader.getPage(i)
            text += page.extractText()
        pdf_file.close()
        print(text)
        
    case default:
        print("select no. only from 0 to 10 only")

# code by sarvesh@2004



























# code by sarvesh@2004
        
