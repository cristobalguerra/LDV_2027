# mallaldv27 — Documento maestro del proyecto

**Licenciatura en Diseño Visual y Negocios Creativos · Plan 2027**
Universidad de Monterrey · Centro Roberto Garza Sada de Arte, Arquitectura y Diseño (CRGS)
Última actualización del documento: 15 de julio de 2026

---

## 0 · Qué es este proyecto

Una **aplicación web autocontenida** (un solo `index.html`) que sirve como expediente vivo de la propuesta de cambio de nombre del programa:

> **De:** Licenciatura en Diseño Gráfico → **A:** Licenciatura en Diseño Visual y Negocios Creativos

La app presenta el mapa curricular del Plan 2027, el programa académico, el certificado y —lo central de este proyecto— la pestaña **Congruencia**, que sustenta con evidencia cuantitativa y documental por qué el nombre corresponde al contenido del plan y por qué el programa debe permanecer adscrito a la Escuela de Arte y Diseño.

---

## 1 · Ubicación, ejecución y despliegue

| Recurso | Valor |
|---|---|
| **Repo local** | `/Volumes/Lexar/ldv-2027/` |
| **Archivo principal** | `index.html` (vanilla HTML + CSS + JS, ~5,500 líneas) |
| **GitHub** | https://github.com/cristobalguerra/LDV_2027 *(antes `LDGD_UDEM` — la URL vieja murió al renombrar)* |
| **GitHub Pages** | https://cristobalguerra.github.io/LDV_2027/ |
| **Servidor local** | `npx http-server /Volumes/Lexar/ldv-2027 -p 8027 -c-1` → `http://localhost:8027` |
| **Backend** | Firebase Realtime Database `ldgd-udem` (fallback a `localStorage`) |
| **Contraseña admin** | `ldv2027` (acceso al modo de edición) |

> **Nota de red:** si Pages "no abre", suele ser bloqueo de ruta hacia el CDN de GitHub (`185.199.x.x`) desde ciertas redes/hotspots — no es falla del sitio. Verificar desde otra red o con el espejo `https://cdn.jsdelivr.net/gh/cristobalguerra/LDV_2027@main/index.html`.

> **Gotcha exFAT:** el volumen Lexar es exFAT; el HMR de dev servers muere ahí. Por eso se sirve con `http-server` estático y se recarga a mano.

---

## 2 · Identidad visual

- **Fondo:** negro `#000`
- **Diseño Visual (acento principal):** lima `#D3F42B` — reemplazó al amarillo institucional `#FFF500` en toda la app
- **Negocios Creativos:** violeta `#7A3BE8`
- **Ejes** (familia de los dos colores): Lenguaje Visual = lima · Producción y Gestión = verde `#8FD94E` · Sistemas e Identidad = lavanda `#A793E0` · Experiencia e Interacción = violeta `#7A3BE8` · Dirección Estratégica = violeta profundo `#6F5BB5`
- **Niveles B/I/A/E** (dominio): B violeta profundo → I lavanda → A verde → E lima
- **Tipografías:** Raleway (títulos), DM Sans (texto), JetBrains Mono (datos/código)

---

## 3 · Estructura de la app (pestañas)

Entrada: pantalla de login con "Ver Programa" (viewer) o contraseña (admin).

1. **Programa** — Fines de aprendizaje, perfil de egreso/ingreso, 6 competencias (SLOs), trayecto formativo B/I/A/E.
2. **Mapa** — Malla de 9 semestres, 46 tarjetas (36 materias profesionales + Formación UDEM + Conocimiento General), agrupadas en 5 fases. Filtros por eje / tipo / competencia. Franja izquierda de cada tarjeta = **tipo de materia** (Estudio, Disciplinar, Sinergia, Certificado, Proyecto, Prácticas); puntos = **ejes que trabaja**. Leyenda al pie. Modal de plan analítico por materia (editable en admin), seriación al hover, drag&drop admin, export PDF.
3. **Congruencia** — El expediente de sustento (ver §5).
4. **Certificado** — La credencial "Diseño Estratégico y Dirección Creativa".
5. *(Ocultas)* Investigación, Validación (instrumento de semáforo), Gestión de cambios (admin).

---

## 4 · Nombres oficiales SEP

Las 36 materias profesionales llevan los nombres oficiales de la **Matriz Curricular (julio 2026)**, sincronizados en el HTML y en Firebase. Se conservaron aliases de slugs para no romper planes/competencias guardados. Backups pre-cambio en `backups/` (excluidos de Git por contener datos de evaluadores).

### Malla por semestre (con % de intensidad DV/NC — matriz validada 59/41)

```
S1  Estudio de Diseño Visual · Visualización y Pensamiento de Diseño ·
    Contexto Cultural del Diseño · Herramientas Digitales para el Diseño
S2  Estudio de Forma, Color y Estructura · Principios de la Tipografía ·
    Ilustración Aplicada · Lenguaje y Significado en el Diseño
S3  Estudio de Identidad, Forma y Significado · Fundamentos de Diseño de Información ·
    Fotografía para Diseño · Tipografía Aplicada ·
    Dirección de Arte para Medios Audiovisuales e Interactivos
S4  Estudio de Información y Visualización · Producción de Diseño y Prototipos ·
    Diseño de Empaque · [C] Dirección de Arte y Fotografía de Producto ·
    [C] Gestión de Proyectos Creativos
S5  Estudio de Marca y Sistemas Visuales · Portafolio Profesional ·
    Materiales Experimentales · [C] Dirección Visual de Marca
S6  Estudio de Diseño de Interacción · Diseño de Experiencia · Diseño de Interfaz ·
    Estrategia de Negocios para Arte y Diseño · [C] Animación Gráfica y Contenido Digital
S7  Estudio de Estrategia y de Servicios · Prácticas Profesionales ·
    Metodología de Investigación y Creación para el Arte y Diseño ·
    [C] Inteligencia Artificial Aplicada al Diseño Visual
S8  Estudio Integral de Diseño Visual y Negocios Creativos · Programa de Evaluación Final I ·
    Diseño Participativo · [C] De la Idea Gráfica al Mercado
S9  Programa de Evaluación Final II
```
`[C]` = materia del Certificado. Total: 324 créditos, 9 semestres.

---

## 5 · Pestaña Congruencia — arco de argumentación

El orden narrativo, sección por sección:

1. **Hero — el número.** Barra bicolor animada: **59.0% Diseño Visual / 41.0% Negocios Creativos**. Lectura: *"la denominación del programa corresponde al contenido del plan."*
2. **Fundamentación disciplinar.** Por qué el negocio pertenece al diseño sin volverse administración. Cita de la **World Design Organization** firmada con su logo en blanco.
3. **El modelo ya existe.** Benchmark institucional: **Parsons** (BBA Strategic Design and Management), **UAL** (BA Design Management), **CENTRO** (Lic. en Negocios e Industrias Creativas, destacada con **RVOE SEP Federal 20254146**) — todas bajo escuelas de diseño, no de administración.
4. **El Certificado propio.** La licenciatura otorga su credencial "Diseño Estratégico y Dirección Creativa": 6 materias, 36 créditos, sems 4–8, **50% de intensidad promedio en Negocios Creativos** (el bloque más denso del plan).
5. **Quiénes respaldan.** Consejo consultivo (3) + claustro (5), con foto, cargo y credenciales.
6. **Distribución.** Las 36 materias: **19 predominio Diseño Visual · 10 integración · 7 predominio Negocios Creativos**.
7. **Competencias.** Las 6 competencias de egreso (SLOs) reciben aportación de ambos dominios.
8. **Evidencia y metodología.** 5 anexos desplegables con iconos: espectro (butterfly de 36 materias), matriz heatmap 0–3, dimensiones (27), detalle por SLO, metodología. Ficha drill-down por materia.

---

## 6 · El modelo cuantitativo SLO

- **36 materias × 27 dimensiones** (15 de Diseño Visual + 12 de Negocios Creativos), escala **0–3** (0 no aparece · 1 introduce · 2 aplica · 3 resultado central evaluable).
- Vinculación **dimensión → SLO** (pesos 0–3) → alineación curso–SLO (0–100) → nivel **B/I/A/E** por rango → % de contribución.
- 6 SLOs: (1) Dirección estratégica · (2) Comunicación visual · (3) Procesos creativos · (4) Integración tecnológica · (5) Modelos de negocio · (6) Impacto social y cultural.
- Fuente: `Matriz_Curricular_con_Modelo_Matematico_SLO.xlsx`. Modelo embebido en el HTML como `const SLO_MODEL`.

### Tres versiones del modelo (en `Informacion/`)
| Versión | Balance | Qué es |
|---|---|---|
| **v1 (preliminar)** | 51.9 / 48.1 | Calificada por denominación y objetivos |
| **v2 (validada)** | 67.2 / 32.8 | Recalificada leyendo los 35 programas analíticos reales (`slo_model_v2.json`) |
| **v3 (objetivo)** | **59.0 / 41.0** | La que muestra la app hoy; requiere las adiciones del Plan 59/41 (`slo_model_v3.json`) |

**Cómo se llegó a v2:** workflow de 70 agentes (35 auditores + 35 verificadores adversariales) leyó cada programa analítico y corrigió 568 de 972 celdas. Hallazgo: los programas actuales no explicitan el negocio que la matriz preliminar les atribuía (ver `Reporte_Validacion_Matriz.md` y `cambios_matriz.csv` con evidencia citada).

**Cómo se llega a v3:** el `Plan_59-41_Adiciones_Programas.md` lista **146 niveles a sustentar en 28 materias**, redactados como unidades/actividades/criterios listos para el Anexo 3. Prioridad de reescritura: **PEF I y II** (genéricos), luego el Certificado. Al incorporarse al programa, se revalida y el 59/41 se vuelve real y auditable.

---

## 7 · Las personas (sección "Quiénes respaldan")

### Consejo consultivo — representantes del sector creativo
- **Vicky González** — Fundadora de VVORKROOM · ex alumna de Diseño Gráfico UDEM, ex codirectora de Futura, +20 años de branding en +15 países.
- **Álex López** — Fundador de Plural Branding · alumni UDIT; clientes WOW Concept, Inditex, Picnic, Toledo.
- **Ferran Ollé** — Cofundador de Faena Studio · Best Branding Awards (Spotify "Mexcla"), LADAWARDS; co-dirige el FAENA Bootcamp con la UDEM.

### Claustro — perfiles de negocio
- **Eduardo Guizar Vukovich** — Director del Departamento de Diseño y Multimedia · posgrados en Comunicaciones y Psicología, imagen institucional corporativa, co-desarrolló un MBA.
- **Cristóbal Rodolfo Guerra Tamez** — Director del Programa de Diseño Gráfico · Doctor SNII, Maestría en Gestión e Innovación del Diseño, cátedra en la Escuela de Negocios del Tec, investigación en comportamiento del consumidor.
- **Marco Vinicio Garrido-Félix** — Decano Asociado de Asuntos Internacionales; fundó sedes CRGS Satélite NY, Barcelona, Oaxaca; jurado internacional.
- **Iliana Moreno** — MA en Administración de Diseño (Southampton); docente de Emprendimiento e Incubación de Negocios.
- **Rolando Angulo** — Master en Branding (ELISAVA); dirige su propio estudio desde 2007; vincula sus cursos con clientes reales.

### Validación institucional
Comité Curricular, Academia y Presidencia del Consejo Consultivo del CRGS — **Sra. Kana Fernández Garza**.

---

## 8 · Backend Firebase (`ldgd-udem`)

Nodos bajo `ldgd/`: `customizations` (nombres/tipos/créditos por tarjeta), `layout` (orden por semestre), `plans` (planes analíticos), `prereqs` (seriación por nombre), `validations` (respuestas del instrumento de semáforo), `changeLog`, `bank`.

Llaves derivan del slug del nombre + posición (`slug--sNpM`). **Renombrar materias exige migrar Firebase** (ya hecho para los nombres oficiales; backup completo en `backups/`).

---

## 9 · Archivos del repo

```
index.html                         La app completa
fotos/                             Fotos del consejo/claustro + logos (Parsons, UAL, CENTRO)
mallaldv27.md                      Este documento
handoff.md                         Bitácora previa (mapeo de nombres confirmado por dirección)
Informacion/
  slo_model_v2.json                Modelo validado (67.2/32.8)
  slo_model_v3.json                Modelo objetivo (59/41) — el de la app
  Reporte_Validacion_Matriz.md     Brechas por materia vs programas reales
  Plan_59-41_Adiciones_Programas.md  Las 146 adiciones por programa para sostener 59/41
  cambios_matriz.csv               568 correcciones con evidencia citada
  planes_2026-07/                  Los 35 programas analíticos (docx + txt)
  Etapa 3_*                        Material de Anexo 3, taxonomía de Bloom
Planes_Analiticos/                 Planes analíticos previos
backups/  (git-ignored)            Respaldos Firebase + index — contienen datos de evaluadores
```

---

## 10 · Pendientes

- [ ] **Reescribir programas analíticos** con las adiciones del Plan 59/41 (prioridad: PEF I/II, luego Certificado). Al terminar, re-correr la auditoría para confirmar el 59/41.
- [ ] Completar en la caja de Validación los **números** de profesores/alumnos/prospectos/exalumnos consultados.
- [ ] Decidir si las pestañas ocultas (Investigación/Validación/Gestión) se retiran o reactivan.
- [ ] Confirmar con dirección el único mapeo débil: *Diseño Participativo* ↔ sinergia de S8.
- [ ] Armar el **slide físico** (HTML→PDF o PPTX) de propuesta de cambio de nombre a partir de estas secciones.

---

## 11 · Fuentes citadas en el expediente

World Design Organization · UNESCO (industrias culturales y creativas) · INEGI, Cuenta Satélite de la Cultura 2024 (Diseño y servicios creativos = 14.5% del PIB cultural, +7.7% anual) · IMCO Compara Carreras · Data México · Parsons, UAL, SCAD, CENTRO (RVOE SEP 20254146) · Matriz de congruencia curricular UDEM.

---

*Documento de uso interno. Generado como referencia integral del proyecto LDV Plan 2027.*
