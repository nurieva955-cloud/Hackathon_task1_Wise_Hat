"""
Вспомогательные функции для приложения
"""

import streamlit as st
from typing import List, Optional
from universities_data import University
import os


def display_university_card(university: University, cols=None):
    """Отображает карточку университета"""
    if cols is None:
        cols = st.columns([1, 2])

    with cols[0]:
        # Проверяем наличие фото
        photo_path = f"university_photos/{university.photo_filename}"
        if os.path.exists(photo_path):
            st.image(photo_path, use_column_width=True)
        else:
            st.image("https://via.placeholder.com/300x200?text=University+Photo",
                     caption="Фото будет загружено", use_column_width=True)

    with cols[1]:
        st.subheader(university.name)

        # Рейтинг звездочками
        stars = "⭐" * int(university.rating)
        st.caption(f"{stars} {university.rating}/10 | 🏙️ {university.city} | 🎓 {university.type}")

        # Краткое описание
        st.write(university.description[:150] + "...")

        # Кнопка для перехода на страницу университета
        if st.button("Подробнее", key=f"btn_{university.id}"):
            st.session_state.selected_university = university.id
            st.rerun()

        # Быстрые ссылки
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"📞 {university.phone}")
        with col2:
            st.markdown(f"🌐 [{university.website}]({university.website})")
        with col3:
            st.markdown(f"📧 {university.contact_email}")


def create_university_page(university: University):
    """Создает страницу для университета"""
    st.title(university.name)

    # Две колонки для фото и основной информации
    col1, col2 = st.columns([1, 2])

    with col1:
        photo_path = f"university_photos/{university.photo_filename}"
        if os.path.exists(photo_path):
            st.image(photo_path, use_column_width=True)
        else:
            st.warning("Фото университета еще не загружено")
            st.info("Загрузите фото в папку university_photos")

    with col2:
        # Рейтинг и основная информация
        st.subheader("📊 Основная информация")
        col_info1, col_info2, col_info3 = st.columns(3)

        with col_info1:
            st.metric("Рейтинг", f"{university.rating}/10")
            st.metric("Год основания", university.founding_year)

        with col_info2:
            st.metric("Количество студентов", f"{university.students_count:,}")
            st.metric("Бюджетных мест", university.budget_places)

        with col_info3:
            st.metric("Тип", university.type)
            st.metric("Город", university.city)

    # Разделитель
    st.divider()

    # Детальная информация
    col_details1, col_details2 = st.columns(2)

    with col_details1:
        st.subheader("🎯 Специальности")
        for specialty in university.specialties:
            st.markdown(f"• {specialty}")

        st.subheader("✨ Особенности")
        for feature in university.features:
            st.markdown(f"✓ {feature}")

    with col_details2:
        st.subheader("📞 Контакты")
        st.markdown(f"**Адрес:** {university.address}")
        st.markdown(f"**Телефон:** {university.phone}")
        st.markdown(f"**Email:** {university.contact_email}")
        st.markdown(f"**Веб-сайт:** [{university.website}]({university.website})")

    st.divider()

    # Полное описание
    st.subheader("📖 Подробное описание")
    st.write(university.description)

    # Кнопка для возврата
    if st.button("← Назад к поиску"):
        st.session_state.selected_university = None
        st.rerun()


def search_universities_advanced(query: str, city: str = "", uni_type: str = "") -> List[University]:
    """Расширенный поиск университетов"""
    from universities_data import get_all_universities, search_universities

    all_unis = get_all_universities()
    results = []

    for uni in all_unis:
        matches = True

        # Поиск по текстовому запросу
        if query:
            query_lower = query.lower()
            text_match = (
                    query_lower in uni.name.lower() or
                    query_lower in uni.description.lower() or
                    query_lower in ' '.join(uni.specialties).lower() or
                    query_lower in uni.city.lower()
            )
            if not text_match:
                matches = False

        # Фильтр по городу
        if city and uni.city.lower() != city.lower():
            matches = False

        # Фильтр по типу
        if uni_type and uni_type != "любой" and uni.type.lower() != uni_type.lower():
            matches = False

        if matches:
            results.append(uni)

    return results


def init_session_state():
    """Инициализация состояния сессии"""
    if 'selected_university' not in st.session_state:
        st.session_state.selected_university = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'ai_initialized' not in st.session_state:
        st.session_state.ai_initialized = False