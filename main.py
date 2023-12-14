import speech_recognition as sr

def reconocer_voz():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo:")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"Has dicho: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print(f"Error en la solicitud a Google Speech Recognition: {e}")
            return None

if __name__ == "__main__":
    palabra_objetivot = "trabajo"
    palabra_objetivod = "descanso"
    palabra_objetivop = "permiso"
    palabra_objetivoe = "enfermedad"
    palabra_objetivov = "vacaciones"
    palabra_objetivoc = "castigo"

    contadort = 0
    contadord = 0
    contadorp = 0
    contadore = 0
    contadorv = 0
    contadorc = 0

    while True:
        comando = reconocer_voz()

        if comando == "adios":
            print("Programa TERMINADO.")
            break
        elif palabra_objetivot in comando:
            contadort += 1
            print(f"Contador incrementado. Valor actual: {contadort}")
        elif palabra_objetivod in comando:
            contadord += 1
            print(f"Contador incrementado. Valor actual: {contadord}")
        elif palabra_objetivop in comando:
            contadorp += 1
            print(f"Contador incrementado. Valor actual: {contadorp}")
        elif palabra_objetivoe in comando:
            contadore += 1
            print(f"Contador incrementado. Valor actual: {contadore}")
        elif palabra_objetivov in comando:
            contadorv += 1
            print(f"Contador incrementado. Valor actual: {contadorv}")
        elif palabra_objetivoc in comando:
            contadorc += 1
            print(f"Contador incrementado. Valor actual: {contadorc}")
        else:
            print("Comando no reconocido. Intenta de nuevo")

    print(f"El vaor final del contador de trabajo es: {contadort}")
    print(f"El vaor final del contador de descanso es: {contadord}")
    print(f"El vaor final del contador de permiso es: {contadorp}")
    print(f"El vaor final del contador de enfermedad es: {contadore}")
    print(f"El vaor final del contador de vacaciones es: {contadorv}")
    print(f"El vaor final del contador de castigo es: {contadorc}")