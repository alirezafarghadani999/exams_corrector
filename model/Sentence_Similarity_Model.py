from sentence_transformers import SentenceTransformer,util

class Sentence_Similarity:
    def __init__(self,main_text,texts):
        self.main= main_text
        self.texts= texts

    def predict(self):

        model = SentenceTransformer('ahdsoft/persian-sentence-transformer-news-wiki-pairs-v3')
        embeddings1 = model.encode(self.main , convert_to_tensor=True)
        embeddings2 = model.encode(self.texts , convert_to_tensor=True)

        cosine_scores = util.cos_sim(embeddings1, embeddings2)

        for i in range(len(self.main)):
            print("{} \t\t {} \t\t Score: {:.4f}".format(
                self.main[i], self.texts[i], cosine_scores[i][i]
            ))




main = [
    # "نیان کارکرد این اختراع بر روی پدیدهٔ تحول میدان‌های الکتریکی و مغناطیسی مبتنی است. نیکلا تسلا از ژنراتورهای خاصی استفاده کرده است که موجب ایجاد میدان‌های الکتریکی و مغناطیسی قوی می‌شوند. این میدان‌ها به صورت بی‌سیم انتقال پیدا می‌کنند و در نقاط مختلف، دستگاه‌های دریافت‌کننده این میدان‌ها قرار دارند.در دستگاه دریافت‌کننده، این میدان‌های الکتریکی و مغناطیسی به یک تبدیل‌کننده تبدیل می‌شوند و به انرژی الکتریکی تبدیل می‌گردند. این انرژی سپس برای تأمین نیازهای برقی دستگاه یا سیستم مصرفی مورد استفاده قرار می‌گیرد"
# "احتیاج دائمی انسان به داشتن برنامه ای که پاسخگوی نیازهایش باشد و سعادت او را تضمین کند"
"""
کاش از اول می دونستم
تو کدوم کوهی که خورشید
از تو چشم تو می تابه
چشمه چشمه ابر ایثار
روی سینه ی تو خوابه
تو کدوم خلیج سبزی
که عمیق اما زلاله
مثل اینه پاک و روشن
مهربون مثل خیاله
"""
]
texts = [
    # " توسط ایجاد میدانهای مغناطیسی و الکتریوی که بوسیله ژنراتورهای خاصیایجاد میشوند باعث تبادل انرژی از جایی به جایدیگر میشوند "
    # "احتیاج دائمی انسان به داشتن برنامه ای که پاسخگوی نیازهایش باشد و سعادت او را تضمین می کند"
    """
کاس ارادل می دوذ
و کد وج کو هی که خو ر شید
از تو چشم تو می تابه
چشمه چشمه ابر ایثار
سره ی یر شیر ی
د راکش ام کار وسرزوی
که عمیق »اما زلاله
مثل اینه پا ک و ررشن
مهر برن مثل خیا له
    """
]
Sentence_Similarity(main,texts).predict()
