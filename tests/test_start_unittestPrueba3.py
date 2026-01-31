import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


# PARTE 1: Pruebas de búsqueda múltiple con find_elements (NAME, CLASS_NAME, CSS_SELECTOR, ID)
class TestParte1(unittest.TestCase):
    """Primera parte de las pruebas - find_elements con NAME, CLASS_NAME, CSS_SELECTOR, ID"""

    def setUp(self):
        """Método de inicio de prueba (Setup)"""
        # Crear una nueva instancia del navegador Microsoft Edge
        self.driver = webdriver.Edge()
        
        # Navegar a la web
        self.driver.get("https://idkjose.github.io/PaginaPruebas/")

    def testName(self):
        """Busca varios elementos en la página por NAME"""
        elementos = self.driver.find_elements(By.NAME, "ultimo")
        
        # Verifica si los elementos fueron encontrados
        if elementos is not None:
            print("Las celdas fueron encontradas")
            for celda in elementos:
                print(celda.text)

    def testClassName(self):
        """Busca varios elementos en la página por CLASS_NAME"""
        elementos = self.driver.find_elements(By.CLASS_NAME, "rojo")
        
        # Verifica si los elementos fueron encontrados
        if elementos is not None:
            print("El elemento by CLASS_NAME rojo fue encontrado")
            for celda in elementos:
                print(celda.text)

    def testCssSelector(self):
        """Busca varios elementos en la página por CSS_SELECTOR"""
        elementos = self.driver.find_elements(By.CSS_SELECTOR, ".rojo")
        
        # Verifica si los elementos fueron encontrados
        if elementos is not None:
            print("Los elementos por CSS_SELECTOR fueron encontrados")
            for celda in elementos:
                print(celda.text)

    def testId(self):
        """Busca varios elementos en la página por ID"""
        elementos = self.driver.find_elements(By.ID, "noImportante")
        
        # Verifica si los elementos fueron encontrados
        if elementos is not None:
            print("El elemento by ID fue encontrado")
            for celda in elementos:
                print(celda.text)

    def tearDown(self):
        """Método para cerrar el driver (Teardown)"""
        self.driver.quit()


# PARTE 2: Pruebas de búsqueda múltiple con find_elements (LINK_TEXT, PARTIAL_LINK_TEXT, TAG_NAME, XPATH)
class TestParte2(unittest.TestCase):
    """Segunda parte de las pruebas - find_elements con LINK_TEXT, PARTIAL_LINK_TEXT, TAG_NAME, XPATH"""

    def setUp(self):
        """Método de inicio de prueba (Setup)"""
        # Crear una nueva instancia del navegador Microsoft Edge
        self.driver = webdriver.Edge()
        
        # Navegar a la web
        self.driver.get("https://idkjose.github.io/PaginaPruebas/")

    def testLinkText(self):
        """Busca varios elementos en la página por LINK_TEXT"""
        elementos = self.driver.find_elements(By.LINK_TEXT, "Pagina 2")
        
        # Verifica si los elementos fueron encontrados
        if elementos is not None:
            print("El elemento by LINK_TEXT fue encontrado")
            for celda in elementos:
                print(celda.text)

    def testPartialLinkText(self):
        """Busca varios elementos en la página por PARTIAL_LINK_TEXT"""
        elementos = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "Pagina")
        
        # Verifica si los elementos fueron encontrados
        if elementos is not None:
            print("Los elementos by PARTIAL_LINK_TEXT fueron encontrados")
            for celda in elementos:
                print(celda.text)

    def testTagName(self):
        """Busca varios elementos en la página por TAG_NAME"""
        elementos = self.driver.find_elements(By.TAG_NAME, "td")
        
        # Verifica si los elementos fueron encontrados
        if elementos is not None:
            print("Los elementos por TAG_NAME fueron encontrados")
            for celda in elementos:
                print(celda.text)

    def testXpath(self):
        """Busca varios elementos en la página por XPATH"""
        elementos = self.driver.find_elements(By.XPATH, "//td[@class='rojo']")
        
        # Verifica si los elementos fueron encontrados
        if elementos is not None:
            print("Los elementos por XPATH fueron encontrados")
            for celda in elementos:
                print(celda.text)

    def tearDown(self):
        """Método para cerrar el driver (Teardown)"""
        self.driver.quit()


if __name__ == "__main__":
    # Crear suite de pruebas para Parte 1
    suite_parte1 = unittest.TestLoader().loadTestsFromTestCase(TestParte1)
    
    # Ejecutar Parte 1
    print("\n=== EJECUTANDO PARTE 1: ID y NAME ===")
    runner_parte1 = unittest.TextTestRunner(verbosity=2)
    resultado_parte1 = runner_parte1.run(suite_parte1)
    
    # Crear suite de pruebas para Parte 2
    suite_parte2 = unittest.TestLoader().loadTestsFromTestCase(TestParte2)
    
    # Ejecutar Parte 2
    print("\n=== EJECUTANDO PARTE 2: CLASS_NAME y LINK_TEXT ===")
    runner_parte2 = unittest.TextTestRunner(verbosity=2)
    resultado_parte2 = runner_parte2.run(suite_parte2)
    
    # Mostrar resumen
    print("\n=== RESUMEN DE PRUEBAS ===")
    print(f"Parte 1 - Ejecutadas: {resultado_parte1.testsRun}, Fallidas: {len(resultado_parte1.failures)}, Errores: {len(resultado_parte1.errors)}")
    print(f"Parte 2 - Ejecutadas: {resultado_parte2.testsRun}, Fallidas: {len(resultado_parte2.failures)}, Errores: {len(resultado_parte2.errors)}")

