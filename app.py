import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Настройка API (Вставь сюда свой ключ)
GOOGLE_API_KEY = "YOUR_APIKEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Настройка страницы
st.set_page_config(page_title="AI Шеф-повар", page_icon="🍳")
st.title("🍳 AI Шеф-повар: Рецепт по фото")
st.write("Сфоткай холодильник, а я скажу, что приготовить!")

# 2. Загрузка фото
uploaded_file = st.file_uploader("Выберите фото продуктов...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Показываем фото пользователю
    image = Image.open(uploaded_file)
    st.image(image, caption='Твои продукты', use_container_width=True)

    # Кнопка запуска
    if st.button('Что приготовим?'):
        model = genai.GenerativeModel('gemini-2.5-flash')

        # Промпт для нейронки
        prompt = """
        Посмотри на это фото продуктов. 
        1. Перечисли, что ты видишь.
        2. Придумай ОДНО конкретное блюдо, которое можно из этого приготовить.
        3. Напиши краткий рецепт по шагам.
        Будь кратким, дружелюбным и используй эмодзи.
        """

        with st.spinner('Нейрошеф думает...'):
            try:
                # Отправляем картинку и текст в нейронку
                response = model.generate_content([prompt, image])

                st.subheader("👨‍🍳 Вердикт шефа:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Ошибка: {e}. Проверь API ключ!")

# Инструкция по запуску внизу

st.info("Чтобы запустить: напиши в терминале 'streamlit run app.py'")
