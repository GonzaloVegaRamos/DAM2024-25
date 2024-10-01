import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class EjecutarComando {
    public static void main(String[] args) {
        // Creamos un objeto ProcessBuilder que ejecutará el comando "ls" (Linux/macOS) o "dir" (Windows)
        ProcessBuilder processBuilder = new ProcessBuilder();

        // Dependiendo del sistema operativo, usaremos diferentes comandos
        if (System.getProperty("os.name").toLowerCase().contains("win")) {
            processBuilder.command("cmd.exe", "/c", "dir");
        } else {
            processBuilder.command("sh", "-c", "ls");
        }

        try {
            // Iniciar el proceso
            Process process = processBuilder.start();

            // Leer la salida del comando
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String linea;
            while ((linea = reader.readLine()) != null) {
                System.out.println(linea);
            }

            // Esperar a que el proceso termine y obtener el código de salida
            int exitCode = process.waitFor();
            System.out.println("\nEl proceso terminó con el código: " + exitCode);

        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

