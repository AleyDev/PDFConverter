# 'pdf2docx' kütüphanesinden 'Converter' sınıfını içe aktarıyorum.

from pdf2docx import Converter  


# Dönüştürmek istediğim PDF dosyasının yolunu burada belirliyorum. (Örneğin, "sample.pdf")
pdf_path = "sample.pdf"

# Oluşacak DOCX dosyasının yolunu burada belirliyorum. (Örneğin, "sample.docx")
docx_path = "sample.docx"

# 'Converter' sınıfını kullanarak PDF dosyasını DOCX formatına dönüştürmek için bir nesne oluşturuyorum.
cv = Converter(pdf_file=pdf_path)  # 'pdf_file' parametresine dönüştürülecek PDF dosyasının yolunu veriyorum.

# 'convert' metodunu çağırarak PDF dosyasını DOCX formatına dönüştürüyorum.
cv.convert(docx_filename=docx_path)  # 'docx_filename' parametresine çıktının kaydedileceği DOCX dosyasının yolunu veriyorum.

# İşlem tamamlandıktan sonra hafızadan manuel olarak kapatıyorum.
cv.close()  # 'close' metodunu çağırarak 'Converter' nesnesini kapatıyorum. Bu, bellekteki kaynakları serbest bırakır.
