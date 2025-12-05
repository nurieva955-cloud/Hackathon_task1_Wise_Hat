"""
Модель данных для университетов Казахстана
"""

from dataclasses import dataclass
from typing import List, Optional, Dict, Any
import pandas as pd


@dataclass
class University:
    """Класс для хранения информации об университете"""
    id: str
    name: str
    name_eng: str
    city: str
    description: str
    type: str  # "технический", "медицинский", "гуманитарный", "национальный", "исследовательский", "международный"
    rating: float  # 1-10
    founding_year: int
    students_count: int
    budget_places: int
    contact_email: str
    website: str
    address: str
    phone: str
    specialties: List[str]
    photo_filename: str  # имя файла с фото в папке university_photos
    features: List[str]  # ключевые особенности

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'name_eng': self.name_eng,
            'city': self.city,
            'description': self.description,
            'type': self.type,
            'rating': self.rating,
            'founding_year': self.founding_year,
            'students_count': self.students_count,
            'budget_places': self.budget_places,
            'contact_email': self.contact_email,
            'website': self.website,
            'address': self.address,
            'phone': self.phone,
            'specialties': ', '.join(self.specialties),
            'photo_filename': self.photo_filename,
            'features': ', '.join(self.features)
        }


# Данные университетов
UNIVERSITIES = [
    University(
        id="enu",
        name="Евразийский национальный университет имени Л.Н. Гумилева",
        name_eng="L.N. Gumilyov Eurasian National University",
        city="Астана",
        description="Ведущий национальный исследовательский университет Казахстана, основанный в 1996 году. Университет сочетает в себе лучшие традиции евразийской науки и образования.",
        type="национальный",
        rating=9.2,
        founding_year=1996,
        students_count=17000,
        budget_places=4500,
        contact_email="info@enu.kz",
        website="https://enu.kz",
        address="г. Астана, ул. Сатпаева, 2",
        phone="+7 (7172) 70-95-00",
        specialties=["Инженерия", "IT", "Международные отношения", "Филология", "Юриспруденция"],
        photo_filename="enu.jpg",
        features=["Ведущий национальный вуз", "Сильная исследовательская база", "Международные партнерства"]
    ),
    University(
        id="nu",
        name="Назарбаев Университет",
        name_eng="Nazarbayev University",
        city="Астана",
        description="Международный исследовательский университет мирового уровня, основанный в 2010 году. Является флагманом высшего образования в Казахстане.",
        type="международный",
        rating=9.8,
        founding_year=2010,
        students_count=6000,
        budget_places=2000,
        contact_email="admissions@nu.edu.kz",
        website="https://nu.edu.kz",
        address="г. Астана, пр. Кабанбай батыра, 53",
        phone="+7 (7172) 70-60-00",
        specialties=["Инженерия", "Медицина", "Бизнес", "Гуманитарные науки", "IT"],
        photo_filename="nu.jpg",
        features=["Обучение на английском", "Международный преподавательский состав", "Исследовательский фокус"]
    ),
    University(
        id="astana_med",
        name="Медицинский университет Астана",
        name_eng="Astana Medical University",
        city="Астана",
        description="Современный медицинский университет, готовящий высококвалифицированных специалистов для системы здравоохранения Казахстана.",
        type="медицинский",
        rating=8.5,
        founding_year=1964,
        students_count=5000,
        budget_places=1200,
        contact_email="rector@amu.kz",
        website="https://amu.kz",
        address="г. Астана, ул. Бейбитшилик, 49А",
        phone="+7 (7172) 53-94-19",
        specialties=["Лечебное дело", "Стоматология", "Фармация", "Общественное здравоохранение"],
        photo_filename="astana_med.jpg",
        features=["Современные лаборатории", "Клиническая база", "Международные программы"]
    ),
    University(
        id="kazguu",
        name="Университет КАЗГЮУ имени М.С. Нарикбаева",
        name_eng="KazGUU University named after M.S. Narikbayev",
        city="Астана",
        description="Ведущий юридический университет Казахстана, специализирующийся на подготовке юристов международного уровня.",
        type="гуманитарный",
        rating=8.7,
        founding_year=1994,
        students_count=7000,
        budget_places=1800,
        contact_email="info@kazguu.kz",
        website="https://kazguu.kz",
        address="г. Астана, пр. Кошкарбаева, 39",
        phone="+7 (7172) 70-30-30",
        specialties=["Юриспруденция", "Международное право", "Государственное управление", "Бизнес"],
        photo_filename="kazguu.jpg",
        features=["Юридическая специализация", "Английские программы", "Партнерства с зарубежными вузами"]
    ),
    University(
        id="kaznu",
        name="Казахский национальный университет имени аль-Фараби",
        name_eng="Al-Farabi Kazakh National University",
        city="Алматы",
        description="Старейший и крупнейший университет Казахстана, основанный в 1934 году. Входит в топ-500 мировых университетов.",
        type="национальный",
        rating=9.5,
        founding_year=1934,
        students_count=20000,
        budget_places=6000,
        contact_email="info@kaznu.kz",
        website="https://www.kaznu.kz",
        address="г. Алматы, ул. аль-Фараби, 71",
        phone="+7 (727) 377-33-33",
        specialties=["Естественные науки", "IT", "Медицина", "Гуманитарные науки", "Юриспруденция"],
        photo_filename="kaznu.jpg",
        features=["Ведущий классический вуз", "Широкий спектр специальностей", "Сильная исследовательская база"]
    ),
    University(
        id="kaznmu",
        name="Казахский национальный медицинский университет имени С. Д. Асфендиярова",
        name_eng="Asfendiyarov Kazakh National Medical University",
        city="Алматы",
        description="Ведущий медицинский университет страны с богатой историей и современными образовательными стандартами.",
        type="медицинский",
        rating=9.0,
        founding_year=1931,
        students_count=10000,
        budget_places=2500,
        contact_email="info@kaznmu.kz",
        website="https://kaznmu.kz",
        address="г. Алматы, ул. Толе би, 94",
        phone="+7 (727) 338-70-70",
        specialties=["Лечебное дело", "Педиатрия", "Стоматология", "Фармация", "Сестринское дело"],
        photo_filename="kaznmu.jpg",
        features=["Исторический медицинский вуз", "Современные симуляционные центры", "Международные связи"]
    ),
    University(
        id="kbtu",
        name="Казахстанско-Британский технический университет",
        name_eng="Kazakh-British Technical University",
        city="Алматы",
        description="Ведущий технический университет, созданный в партнерстве с британскими университетами. Специализируется на IT и инженерии.",
        type="технический",
        rating=9.1,
        founding_year=2001,
        students_count=8000,
        budget_places=2200,
        contact_email="info@kbtu.kz",
        website="https://kbtu.edu.kz",
        address="г. Алматы, ул. Толе би, 59",
        phone="+7 (727) 272-50-00",
        specialties=["Информационные технологии", "Нефтегазовое дело", "Электроника", "Бизнес-информатика"],
        photo_filename="kbtu.jpg",
        features=["Британские образовательные стандарты", "IT-специализация", "Тесные связи с индустрией"]
    ),
    University(
        id="kimep",
        name="Университет КИМЭП",
        name_eng="KIMEP University",
        city="Алматы",
        description="Ведущий университет в области бизнеса и социальных наук, основанный по американской модели образования.",
        type="международный",
        rating=8.9,
        founding_year=1992,
        students_count=4000,
        budget_places=1000,
        contact_email="admissions@kimep.kz",
        website="https://kimep.kz",
        address="г. Алматы, ул. Абая, 4",
        phone="+7 (727) 270-44-00",
        specialties=["Бизнес-администрирование", "Экономика", "Государственное управление", "Переводческое дело"],
        photo_filename="kimep.jpg",
        features=["Американская модель образования", "Обучение на английском", "Сильная бизнес-школа"]
    ),
    University(
        id="narxoz",
        name="Narxoz University",
        name_eng="Narxoz University",
        city="Алматы",
        description="Ведущий экономический университет Казахстана, специализирующийся на бизнесе, экономике и финансах.",
        type="экономический",
        rating=8.6,
        founding_year=1963,
        students_count=9000,
        budget_places=2000,
        contact_email="info@narxoz.kz",
        website="https://narxoz.kz",
        address="г. Алматы, ул. Жандосова, 55",
        phone="+7 (727) 377-11-11",
        specialties=["Экономика", "Финансы", "Маркетинг", "Менеджмент", "Бухгалтерский учет"],
        photo_filename="narxoz.jpg",
        features=["Экономическая специализация", "Партнерства с бизнесом", "Современные образовательные программы"]
    ),
    University(
        id="kainar",
        name="Казахский национальный аграрный исследовательский университет",
        name_eng="Kazakh National Agrarian Research University",
        city="Алматы",
        description="Ведущий аграрный университет страны, специализирующийся на сельском хозяйстве и пищевых технологиях.",
        type="аграрный",
        rating=8.4,
        founding_year=1929,
        students_count=12000,
        budget_places=3000,
        contact_email="info@kaznaru.kz",
        website="https://kaznaru.edu.kz",
        address="г. Алматы, пр. Абая, 8",
        phone="+7 (727) 291-23-23",
        specialties=["Агрономия", "Ветеринария", "Пищевые технологии", "Лесное хозяйство"],
        photo_filename="kainar.jpg",
        features=["Аграрная специализация", "Исследовательские лаборатории", "Связь с сельским хозяйством"]
    ),
    University(
        id="skou",
        name="Южно-Казахстанский университет имени М. О. Ауэзова",
        name_eng="M.O. Auezov South Kazakhstan University",
        city="Шымкент",
        description="Крупнейший университет южного региона Казахстана, предлагающий широкий спектр образовательных программ.",
        type="универсальный",
        rating=8.2,
        founding_year=1943,
        students_count=15000,
        budget_places=3500,
        contact_email="info@ukgu.kz",
        website="https://ukgu.kz",
        address="г. Шымкент, пр. Тауке хана, 5",
        phone="+7 (7252) 21-34-56",
        specialties=["Педагогика", "Технические науки", "Медицина", "Гуманитарные науки"],
        photo_filename="skou.jpg",
        features=["Крупнейший вуз юга", "Разнообразные специальности", "Региональный центр науки"]
    ),
    University(
        id="kasgu",
        name="Каспийский государственный университет технологий и инжиниринга имени Ш. Есенова",
        name_eng="Sh. Yessenov Caspian University of Technologies and Engineering",
        city="Актау",
        description="Ведущий технический университет западного Казахстана, специализирующийся на нефтегазовых и инженерных технологиях.",
        type="технический",
        rating=8.0,
        founding_year=1963,
        students_count=6000,
        budget_places=1500,
        contact_email="info@kasgu.kz",
        website="https://kasgu.kz",
        address="г. Актау, 32 микрорайон",
        phone="+7 (7292) 50-60-70",
        specialties=["Нефтегазовое дело", "Инженерия", "IT", "Морские технологии"],
        photo_filename="kasgu.jpg",
        features=["Техническая специализация", "Фокус на нефтегаз", "Прибрежное расположение"]
    ),
    University(
        id="argu",
        name="Актюбинский региональный государственный университет имени К. Жубанова",
        name_eng="K. Zhubanov Aktobe Regional State University",
        city="Актобе",
        description="Крупный региональный университет, предлагающий классическое образование по различным направлениям.",
        type="универсальный",
        rating=7.9,
        founding_year=1966,
        students_count=8000,
        budget_places=2000,
        contact_email="rector@argu.kz",
        website="https://argu.kz",
        address="г. Актобе, пр. А. Молдагуловой, 34",
        phone="+7 (7132) 56-78-90",
        specialties=["Педагогика", "Естественные науки", "Технические науки", "Медицина"],
        photo_filename="argu.jpg",
        features=["Классическое образование", "Развитая инфраструктура", "Региональный лидер"]
    ),
    University(
        id="atyrau_uni",
        name="Атырауский университет имени Х. Досмухамедова",
        name_eng="K. Dosmukhamedov Atyrau University",
        city="Атырау",
        description="Крупнейший университет нефтегазового региона, готовящий специалистов для нефтяной промышленности.",
        type="технический",
        rating=8.1,
        founding_year=1950,
        students_count=7000,
        budget_places=1800,
        contact_email="info@atyrauuniversity.kz",
        website="https://atyrauuniversity.kz",
        address="г. Атырау, ул. Студенческая, 1",
        phone="+7 (7122) 31-45-67",
        specialties=["Нефтегазовое дело", "Химическая технология", "Экология", "Экономика"],
        photo_filename="atyrau_uni.jpg",
        features=["Нефтегазовая специализация", "Тесные связи с промышленностью", "Современные лаборатории"]
    ),
    University(
        id="karaganda_uni",
        name="Карагандинский университет имени академика Е.А. Букетова",
        name_eng="E.A. Buketov Karaganda University",
        city="Караганда",
        description="Крупный классический университет центрального Казахстана с богатой историей и традициями.",
        type="универсальный",
        rating=8.3,
        founding_year=1972,
        students_count=11000,
        budget_places=2800,
        contact_email="info@ksu.kz",
        website="https://ksu.kz",
        address="г. Караганда, ул. Университетская, 28",
        phone="+7 (7212) 77-03-52",
        specialties=["История", "Филология", "Математика", "Биология", "Химия"],
        photo_filename="karaganda_uni.jpg",
        features=["Классическое образование", "Сильные гуманитарные программы", "Исследовательская деятельность"]
    ),
    University(
        id="kokshe_uni",
        name="Кокшетауский университет имени Ш. Уалиханова",
        name_eng="Sh. Ualikhanov Kokshetau University",
        city="Кокшетау",
        description="Ведущий университет северного Казахстана, сочетающий классическое образование с современными технологиями.",
        type="универсальный",
        rating=7.8,
        founding_year=1962,
        students_count=6000,
        budget_places=1600,
        contact_email="rector@ku.kz",
        website="https://ku.kz",
        address="г. Кокшетау, ул. Абая, 76",
        phone="+7 (7162) 25-13-24",
        specialties=["Педагогика", "Сельское хозяйство", "Технические науки", "Экономика"],
        photo_filename="kokshe_uni.jpg",
        features=["Многопрофильный вуз", "Развитая материальная база", "Региональные исследования"]
    ),
]


def get_all_universities() -> List[University]:
    """Возвращает список всех университетов"""
    return UNIVERSITIES


def get_university_by_id(university_id: str) -> Optional[University]:
    """Находит университет по ID"""
    for uni in UNIVERSITIES:
        if uni.id == university_id:
            return uni
    return None


def get_universities_by_city(city: str) -> List[University]:
    """Возвращает университеты в указанном городе"""
    return [uni for uni in UNIVERSITIES if uni.city.lower() == city.lower()]


def get_universities_by_type(uni_type: str) -> List[University]:
    """Возвращает университеты указанного типа"""
    return [uni for uni in UNIVERSITIES if uni.type.lower() == uni_type.lower()]


def get_universities_dataframe() -> pd.DataFrame:
    """Возвращает DataFrame со всеми университетами"""
    data = [uni.to_dict() for uni in UNIVERSITIES]
    return pd.DataFrame(data)


def search_universities(query: str) -> List[University]:
    """Простой поиск по названию и описанию"""
    query = query.lower()
    results = []

    for uni in UNIVERSITIES:
        if (query in uni.name.lower() or
                query in uni.description.lower() or
                query in uni.city.lower() or
                query in ' '.join(uni.specialties).lower()):
            results.append(uni)

    return results