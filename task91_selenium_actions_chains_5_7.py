from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Инициализация драйвера
driver = webdriver.Chrome()

# Открыть веб-страницу (замените URL на ваш адрес)
driver.get("https://parsinger.ru/selenium/5.7/2/index.html")

# Найти элемент на странице с использованием локатора By
draggable = driver.find_element(By.ID, "draggable")

# Использование ActionChains для выполнения перетаскивания элемента
actions = ActionChains(driver)

# 1. Переместить блок влево на 100px
actions.drag_and_drop_by_offset(draggable, -100, 0).perform()

# 2. Переместить блок вниз на 100px
actions.drag_and_drop_by_offset(draggable, 0, 100).perform()

# 3. Переместить блок вправо на 100px
actions.drag_and_drop_by_offset(draggable, 100, 0).perform()

# 4. Переместить блок вверх на 100px
actions.drag_and_drop_by_offset(draggable, 0, -100).perform()

# Закрыть браузер после завершения
driver.quit()


#
# ActionChains(driver)(Цепочка действий)
#
# ActionChains(): Это способ автоматизации низкоуровневых взаимодействий, таких как движения мыши, действия с кнопками мыши, нажатие клавиш и взаимодействие с контекстным меню.
#
# ActionChains — класс, предназначенный для автоматизации сложных последовательностей действий пользователя.
#
# # Import
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# # Использование ActionChains для выполнения последовательности действий
#
# actions = ActionChains(driver) # Создаём экземпляр класса ActionChains
# actions.move_to_element(menu)  # Переместить курсор на элемент меню
# actions.click(submenu)         # Кликнуть по подменю
# actions.perform()              # Выполнить накопленные действия
#
# Особенности и преимущества
#
#     Цепочка действий: Одной из ключевых особенностей ActionChains является возможность создания цепочек действий, которые выполняются последовательно. Это позволяет имитировать сложные действия пользователя.
#
#     Гибкость: С помощью ActionChains можно легко комбинировать различные действия, такие как клики, двойные клики, нажатия клавиш и другие, чтобы создать сложные сценарии взаимодействия.
#
#     Точное взаимодействие: Для сценариев, где требуется высокая точность (например, рисование на холсте или игры), ActionChains предоставляет методы для точного управления движением мыши.
#
# Запустите код ниже и понаблюдайте за происходящим.
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# # Инициализация драйвера
# driver = webdriver.Chrome()
#
# # Открыть веб-страницу (замените URL на ваш адрес)
# driver.get("https://parsinger.ru/selenium/5.7/2/index.html")
#
# # Найти элемент на странице с использованием локатора By
# draggable = driver.find_element(By.ID, "draggable")
#
# # Использование ActionChains для выполнения перетаскивания элемента
# actions = ActionChains(driver)
#
# # 1. Переместить блок влево на 100px
# actions.drag_and_drop_by_offset(draggable, -100, 0).perform()
#
# # 2. Переместить блок вниз на 100px
# actions.drag_and_drop_by_offset(draggable, 0, 100).perform()
#
# # 3. Переместить блок вправо на 100px
# actions.drag_and_drop_by_offset(draggable, 100, 0).perform()
#
# # 4. Переместить блок вверх на 100px
# actions.drag_and_drop_by_offset(draggable, 0, -100).perform()
#
# # Закрыть браузер после завершения
# driver.quit()
#
#
# Методы ActionChains(driver)
#
# actions = ActionChains(driver) # Создаём экземпляр класса ActionChains
# element = driver.find_element(By.ID, "draggable") # Находим необходимый элемент/тег
#
#
#
#     action.perform() — Метод используется для выполнения всех сохраненных операций в экземпляре действия класса ActionChains. Запускает всю цепочку действий.
#
#     action.click(element) — Кликает по элементу.
#
#     action.click_and_hold(element) — Удерживает левую кнопку мыши на элементе.
#
#     # Использование ActionChains для удержания левой кнопки мыши на элементе
#     actions = ActionChains(driver)
#     actions.click_and_hold(element_to_hold).perform()
#
#
#
#     action.context_click(element) — Используется для выполнения контекстного щелчка (щелчка правой кнопкой мыши) по элементу.
#
#     action.drag_and_drop(source, target) — Удерживает левую кнопку мыши на исходном элементе, затем перемещается к целевому элементу и отпускает кнопку мыши.
#
#     # Найти исходный и целевой элементы на странице с использованием локаторов By
#     source = driver.find_element(By.ID, "source_element_id")
#     target = driver.find_element(By.ID, "target_element_id")
#
#     # Использование ActionChains для выполнения перетаскивания элемента
#     actions = ActionChains(driver)
#     actions.drag_and_drop(source, target).perform()
#
#         source: Это исходный элемент, который вы хотите перетащить. source представляет собой тег, который вы хотите "взять" или начать перетаскивание. Обычно это элемент, который вы хотите переместить на другое место на веб-странице.
#
#         target: Это целевой элемент, на который или к которому вы хотите перетащить исходный элемент. target представляет собой тег, на который или к которому вы хотите "отпустить" или завершить перетаскивание исходного элемента. Это место назначения, куда вы хотите переместить исходный элемент на веб-странице.
#         ​​​​​​​
#
#
#     action.release(on_element=None)  — Метод release используется для отпускания удерживаемой кнопки мыши на элементе.
#
#         on_element=None: Это параметр, который представляет собой элемент, на котором вы хотите отпустить кнопку мыши. Если этот параметр не указан (по умолчанию None), кнопка мыши будет отпущена на текущем положении курсора. Если вы укажете конкретный элемент в качестве on_element, кнопка мыши будет отпущена на этом элементе.
#
#     action.drag_and_drop_by_offset(source, xoffset, yoffset)  — Удерживает левую кнопку мыши на исходном элементе, затем перемещается к заданному смещению и отпускает кнопку мыши.
#
#     # Использование ActionChains для выполнения перетаскивания элемента на заданное смещение
#     actions = ActionChains(driver)
#     actions.drag_and_drop_by_offset(source_element, 50, 100).perform()  # Перемещает элемент на 50px вправо и 100px вниз
#
#         source: Элемент для мыши.
#         xoffset: X смещение для перехода.
#         yoffset: Y смещение для перехода.
#
#
#
#     action.key_down(value, element) — Отправляет только нажатие клавиши, не отпуская ее. Следует использовать только с клавишами-модификаторами (Control, Alt и Shift).
#
#     # Использование ActionChains для удержания клавиш
#     actions = ActionChains(driver)
#     actions.key_down(Keys.CONTROL, element) \
#            .key_down(Keys.ALT) \
#            .key_down(Keys.SHIFT) \
#            .key_down('T') \
#            .perform()
#
#         value: Параметр представляет собой значение клавиши, которую вы хотите нажать. value может быть любой клавишей на клавиатуре, любыми клавишами (A, B, C и т. д.). Значения для этих клавиш обычно определены в классе Keys в Selenium. Рассматривали в этом степе;
#
#         element: Параметр представляет собой элемент на веб-странице, к которому вы хотите отправить команду нажатия клавиши. Если этот параметр указан, клавиша будет "нажата" на этом конкретном элементе.
#
#
#
#     action.key_up(value, element)  — Метод используется для отпускания нажатой клавиши с помощью метода key_down.
#
#     # После выполнения необходимых действий, не забудьте отпустить клавиши
#     actions.key_up(Keys.CONTROL) \
#            .key_up(Keys.ALT) \
#            .key_up(Keys.SHIFT) \
#            .key_up('T') \
#            .perform()
#
#         value: параметр представляет собой значение клавиши, которую вы хотите отпустить. В контексте функции key_up, value обычно представляет собой константу из класса Keys, которая соответствует определенной клавише на клавиатуре. Например, Keys.CONTROL, Keys.ALT или Keys.SHIFT.
#
#         element:параметр, который представляет собой элемент, на котором вы хотите выполнить действие отпускания клавиши. Если этот параметр указан, клавиша будет отпущена на указанном элементе. Если этот параметр не указан, клавиша будет отпущена на текущем элементе в фокусе.
#
#
#
#     action.move_by_offset(xoffset, yoffset)  — Позволяет перемещать курсор мыши на определенное расстояние от его текущего положения на экране. Это особенно полезно, когда вы хотите выполнить точное перемещение курсора без необходимости ссылаться на конкретный элемент на веб-странице.
#
#     # Использование move_by_offset для перемещения курсора мыши на 50px вправо и 100px вниз
#     actions.move_by_offset(50, 100).perform()
#
#         xoffset: Горизонтальное смещение, на которое вы хотите переместить курсор мыши относительно его текущего положения. Значение может быть положительным (для перемещения вправо) или отрицательным (для перемещения влево).
#
#         yoffset: Вертикальное смещение, на которое вы хотите переместить курсор мыши относительно его текущего положения. Значение может быть положительным (для перемещения вниз) или отрицательным (для перемещения вверх).
#
#
#
#     action.move_to_element(to_element)  — Метод используется для перемещения мыши в середину элемента.
#
#     # Найти элемент на странице, к которому вы хотите переместить курсор
#     menu_element = driver.find_element(By.ID, "menu_item")
#
#     # Использование ActionChains для перемещения курсора к элементу
#     actions = ActionChains(driver)
#     actions.move_to_element(menu_element).perform()
#
#         to_element: Элемент, к которому вы хотите переместить курсор мыши. В контексте функции, to_element должен быть объектом WebElement, который вы хотите указать или на который хотите навести курсор.
#         ​​​​​​​
#
#
#     action.move_to_element_with_offset(to_element, xoffset, yoffset) — Метод используется для перемещения мыши на смещение указанного элемента. Смещения относятся к верхнему левому углу элемента.
#
#     # Переместить курсор мыши на 50px вправо и 30px вниз от верхнего левого угла элемента element_to_hover
#     actions.move_to_element_with_offset(element_to_hover, 50, 30).perform()
#
#         to_element: WebElement, к которому нужно перейти.
#         xoffset: X смещение для перехода.
#         yoffset: Y смещение для перехода.
#
#
#
#     action.pause(seconds) — Метод паузы используется для приостановки всех входящих данных на указанное время в секундах. Метод паузы очень важен и полезен в случае выполнения какой-либо команды, для загрузки которой требуется какой-либо JavaScript, или в подобной ситуации, когда между двумя операциями есть временной промежуток.
#
#
#
#     action.send_keys(Keys.DOWN) — метод используется для отправки ключей текущему элементу в фокусе;
#
#         Keys.DOWN:  - значения  клавиши определены в классе Keys.
#
#
#
#     action.send_keys_to_element(element, *keys_to_send) — метод отправляет нажатие клавиш конкретному элементу, указанному в параметре element.
#
#     # Найти элемент на странице с использованием локатора By
#     input_element = driver.find_element(By.ID, "inputField")
#
#     # Использование ActionChains для отправки нажатия клавиш элементу
#     actions = ActionChains(driver)
#     actions.send_keys_to_element(input_element, "Hello", Keys.SPACE, "World!").perform()
#
#         element: Элемент, к которому вы хотите отправить нажатия клавиш. Это должен быть объект WebElement, который вы уже нашли на веб-странице.
#
#         *keys_to_send: Последовательность клавиш, которые вы хотите отправить к указанному элементу. Вы можете отправить одну или несколько клавиш, используя этот параметр. Клавиши могут быть представлены строками (например, "Hello") или константами из класса Keys (например, Keys.ENTER или Keys.TAB). Звездочка (*) перед keys_to_send в сигнатуре функции указывает на то, что метод может принимать переменное количество аргументов, переданных как отдельные параметры.
#
#
#     action.reset_actions() — Метод очищает действия, которые уже сохранены локально и в ActionChains. Это один из наиболее часто используемых методов, так как после какой-либо операции необходимо сбросить экземпляр ActionChains для выполнения следующей операции.
#
#     ​​​​​​​
#
#     action.scroll_by_amount(delta_x, delta_y) — Метод прокручивает на заданное количество, начало координат находится в верхнем левом углу области просмотра.
#
#     # Использование ActionChains для прокрутки на заданное количество
#     actions = ActionChains(driver)
#     actions.scroll_by_amount(delta_x=50, delta_y=100).perform()  # Прокрутка на 50 пикселей вправо и 100 пикселей вниз
#
#         delta_x: Cмещение по горизонтали. Положительное значение будет прокручивать содержимое вправо, а отрицательное значение — влево.
#
#         delta_y: Cмещение по вертикали. Положительное значение будет прокручивать содержимое вниз, а отрицательное значение — вверх.
#
#

# action.scroll_from_origin(scroll_origin, delta_x, delta_y) — Выполняет прокрутку на указанное расстояние на основе исходного положения.
#
# # Найти элемент на странице с использованием локатора By
# element_to_scroll = driver.find_element(By.ID, "someElement")
# # Создать элемент ScrollOrigin на основе найденного элемента
# scroll_origin = ScrollOrigin.from_element(element_to_scroll)
# # Использование ActionChains для выполнения прокрутки относительно элемента
# actions = ActionChains(driver)
# actions.scroll_from_origin(scroll_origin, 0, 100).perform()  # Прокрутка вниз на 100 пикселей относительно элемента
#
#     scroll_origin: Место, откуда начинается прокрутка (область просмотра или центр элемента) плюс предоставленные смещения.
#
#     delta_x: Расстояние по оси X для прокрутки с помощью колеса. Отрицательное значение прокручивает влево.
#
#     delta_y: Расстояние по оси Y для прокрутки с помощью колеса. Отрицательное значение прокручивает вверх.​​​​​​​
#
#
#     ScrollOrigin — это класс в Selenium, который используется для задания начальной точки (источника) прокрутки при выполнении действий с прокруткой. Он позволяет определить, откуда начнется прокрутка: от центра элемента,
#
#     scroll_origin = ScrollOrigin.from_element(element, x_offset=0, y_offset=0)
#
#     ​​​​​​​ от края области просмотра (viewport),
#
#     scroll_origin = ScrollOrigin.from_viewport(x_offset=0, y_offset=0)
#
#     или с указанием смещений относительно этих точек.
#     Таким образом, ScrollOrigin позволяет точно управлять начальной точкой прокрутки, что полезно при взаимодействии с элементами вне области видимости или при частичной прокрутке экрана.
#     ​​​​​​​
#
# action.scroll_to_element(element) — Метод предназначен для автоматического прокручивания страницы к указанному элементу.
#
# # Найти элемент на странице
# element = driver.find_element(By.ID, "someElement")
#
# # Использование ActionChains для прокрутки к элементу
# actions = ActionChains(driver)
# actions.scroll_to_element(element).perform()
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_2/')
#     div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
#     while True:
#         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
#
        # for x in range(10):
        #         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
# #