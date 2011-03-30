import sys
from pyPdf import PdfFileWriter, PdfFileReader

def mergePDFFiles(outputFile, filesToBeMerged, watermarkOutput=False):
    output = PdfFileWriter()

    if(len(filesToBeMerged) == 0):
        print 'Empty Input File List'
        return;

    for inFile in filesToBeMerged:
        print 'Adding file' + inFile + ' to the output'
       # Read the input PDF file
        input = PdfFileReader(file(inFile, "rb"))
        if input.getIsEncrypted():
        	input.decrypt('')
        # Add every page in input PDF file to output
        for page in input.pages:
            if watermarkOutput:
                background = PdfFileReader(file("watermark.pdf", "rb")).getPage(0)
                # merge in watermark
                page.mergePage(background)
            output.addPage(page)

    print 'Writing the final out put to file system'
    # Out put stream for output file
    outputStream = file(outputFile, "wb")
    output.write(outputStream)
    outputStream.close()


if __name__ == '__main__':
    i = 0
    outputFile = ''
    inputFiles = []
    watermarkOutput = False

    for arg in sys.argv:
        i = i + 1

        # Watermark?
        if arg == '-m':
            watermarkOutput = True

        # Getting out file
        if arg == '-o':
            outputFile = sys.argv[i]
            print 'Output File: ' + outputFile

        # Extracting Input files
        if arg == '-i':
            outfileOptionPos = sys.argv.index('-o')
            if i < outfileOptionPos:
                inputFiles = sys.argv[i: outfileOptionPos]
                filesStr = ",".join(inputFiles).replace(",", " ")
                print 'Input Files: ' + filesStr
            else:
                inputFiles = sys.argv[i:]
                filesStr = ",".join(inputFiles).replace(",", " ")
                print 'Input Files: ' + filesStr

    # Merging PDF files
    print 'Merging PDF Files......'
    mergePDFFiles(outputFile, inputFiles, watermarkOutput)