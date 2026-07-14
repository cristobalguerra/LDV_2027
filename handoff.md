# Handoff · LDV 2027 → Plan 2027 UDEM

**Última sesión activa:** Mayo 2026
**Director:** Cristóbal Guerra · Director LDGD UDEM
**Proyecto:** Rediseño curricular del programa, Etapa 3 (planes analíticos)

---

## #goal

### Objetivo macro
Diseñar, documentar y entregar la propuesta institucional completa del rediseño curricular del programa **Licenciatura en Diseño Visual y Negocios Creativos · Plan 2027** (anteriormente Licenciatura en Diseño Gráfico, Plan 2021) ante:

1. Comité Curricular UDEM (CONAC)
2. SEP / Normatividad UDEM (Anexo 3, RVOE)
3. SACS COC (Substantive Change Notification)
4. Comité de Honestidad Académica (Código de Uso de IA)

### Sub-objetivos activos en esta sesión

1. **Plan analítico oficial UDEM** para cada una de las 46 materias del programa, en formato Anexo 3 (`.docx` con 8 tablas)
2. **Bibliografía básica consolidada** para entregar a Biblioteca CRGS (Excel multi-hoja)
3. **Código de Uso de IA del programa** como pieza interactiva inmersiva (no PDF)
4. **Decisión estratégica de nombre** del programa para minimizar carga SEP + SACS
5. **Documento comparativo** Plan 2021 vs Plan 2027 (perfil, trayectorias, cambios, diferenciadores, % sinergia)

---

## #current_state

### Decisiones tomadas y bloqueadas
- **Escenario B confirmado** para el Certificado Profesional: 6 materias
  1. Dirección de Arte y Fotografía de Producto
  2. Gestión de Proyectos Creativos
  3. Dirección Visual de Marca
  4. Animación Gráfica y Contenido Digital
  5. Inteligencia Artificial Aplicada al Diseño Visual
  6. **Diseño y Negocios Creativos** (renombrada desde "Emprendimiento Creativo")
- **Certificado unificado** sustituye el modelo de 2 concentraciones A/B del plan vigente
- **Departamento UDEM = DV** (Diseño Visual) confirmado por Normatividad
- **Bibliografías pueden incluir títulos en inglés** cuando sean canónicos del campo
- **Reglas UDEM aplicadas:** nombres con solo primera mayúscula, sin dos puntos, sin numeración seriada, sin anglicismos salvo tecnicismos

### Decisión de nombre — CONFIRMADA (2026-05-31)
- **Nombre del programa: `Licenciatura en Diseño Visual y Negocios Creativos`** ✅ confirmado por el director.
- Implicaciones asumidas:
  - SACS = **Opening a New Program**
  - SEP = **Programa nuevo (~12 meses)**
  - % cambio 59-67% (programa nuevo, no modificación)
  - El bloque "Principales cambios" del comparativo se mantiene en clave de **programa nuevo**.
- Verificación: el nombre ya estaba presente y consistente en `index.html`, `certificado-propuesta.html` y `PRD_Certificado_LDV.md` (era el nombre original). Las menciones de "Diseño Gráfico" en esos archivos son referencias a competidores / comparación, NO el nombre del programa. **Cero ediciones necesarias.**

| Opción | % cambio | SACS | SEP | Estado |
|---|---|---|---|---|
| **Diseño Visual y Negocios Creativos** | **59-67%** | **New Program** | **Programa nuevo (12 m)** | **✅ ELEGIDA** |
| Diseño Gráfico y Negocios Creativos | 28-30% | Significant Modification | Modificación (3-6 m) | descartada |
| Solo Diseño Visual | 40-50% | borderline | borderline | descartada |

---

## #files_in_flight

### Carpeta raíz del proyecto
```
/Volumes/Lexar/ldv-2027/
├── index.html                              # Malla curricular interactiva (la app)
├── codigo-ia.html                          # Código de Uso de IA — pieza inmersiva
├── certificado-propuesta.html              # Propuesta visual del Certificado
├── PRD_Certificado_LDV.md                  # PRD Versión 2.0 — Escenario B
├── handoff.md                              # ← este documento
├── LDV-2027_Bibliografia_Basica.xlsx       # Bibliografía consolidada
├── Planes_Analiticos/                      # docx oficiales UDEM Anexo 3
│   ├── 1_DV1NNN_Estudio_de_principios_y_composicion_visual.docx
│   ├── 1_DV1NNN_Visualizacion_y_pensamiento_de_diseno.docx
│   ├── 2_DV1NNN_Estudio_de_forma_color_y_estructura.docx
│   ├── 2_DV1NNN_Ilustracion_aplicada.docx
│   ├── 6_DV3NNN_Estudio_de_diseno_de_interaccion.docx
│   └── 8_DV4NNN_Diseno_y_negocios_creativos.docx
└── Informacion/                            # Referencia institucional UDEM
    ├── 20260324_Avances_E1_vc.pdf
    ├── Etapa 3_ Capacitacion_Anexo3_competencias.pptx.pdf
    ├── Etapa 3_ Guía de apoyo para el llenado del Anexo 3.xlsx
    └── Etapa 3_ TAXONOMiA-DE-BLOOM.jpg
```

### Templates fuente externos al repo
- `/Users/cristobal.guerra/Downloads/8_AD1203 Tendencias en el liderazgo.docx` — template oficial UDEM (8 tablas)
- `/Users/cristobal.guerra/Downloads/61_DX2142_Estudio de Diseño de Interacción.docx` — plan analítico 2021 base para actualización
- Script generador docx: `/tmp/generate_*_plan.py` (un script por materia, se pueden generalizar)
- Script Excel: `/tmp/generate_biblio_xlsx.py` + `/tmp/add_*_biblio.py`

### Firebase
- Proyecto: `ldgd-udem`
- Path principal: `ldgd/customizations` (override de nombres de materias en malla)
- Estado sincronizado con `index.html`

---

## #changed_2026-05-31 · Info de planes analíticos en la malla web

### `index.html` — nuevo objeto `COURSE_DOCS` (35 materias)
- Se agregó `const COURSE_DOCS = {...}` (justo antes de `Object.entries(COURSE_DATA).forEach`) con el contenido oficial extraído de los 35 `.docx` de `~/Downloads/Planes Analíticos 2027_LDV/`.
- Campos por materia: `obj` (Fines de aprendizaje), `cont` (Contenido temático, array), `met` (Actividades conducción + independientes), `evalu` (Criterios de evaluación con %).
- `openModal` parchado: si existe `COURSE_DOCS[slugId]`, prefiere ese contenido oficial sobre `COURSE_DATA` para objetivo/contenido/metodología, y **muestra criterios de evaluación** (antes no se renderizaban).
- NO se tocó `COURSE_DATA`, NO se renombraron cards, NO se escribió en Firebase. `desc` introductorio y competencias se conservan. Respaldo: `index.html.bak`.

### GOTCHA crítico aprendido (clave para futuras sesiones)
- El **nombre mostrado** de cada card viene de las **customizations de Firebase** (`ldgd/customizations`), pero el **`slugId` (id de la card) es estable** y se deriva del nombre ORIGINAL del HTML al cargar (`assignCardIds`). Por eso `COURSE_DATA`/`COURSE_DOCS` se indexan por el `slugId` original, NO por el nombre visible.
- Ejemplos de cards "sinergia" cuyo nombre visible ≠ slugId:
  - "Materiales Experimentales" → slugId `diseño-de-futuros`
  - "Metodologías de Investigación..." → slugId `producción-artística-interdisciplinaria`
  - "Diseño Participativo" → slugId `innovación-en-diseño`
  - "Estrategia de Negocios para Arte y Diseño" → slugId `estrategia-de-negocios-para-el-diseño`
  - "Direc. Arte para Med. Audiovis." → slugId `direc-creat-para-med-audiovis-e-interac`
- Para mapear docs→cards SIEMPRE leer el `dataset.id` real vía DOM (preview_eval), no inferir del HTML estático.

### Mapeo docx → card confirmado por el director (2026-05-31)
- **Terminología:** el tipo **"sinergia"** en la malla = **Eje Formación de Conocimiento General (Optativas)**. Son la misma categoría.
- Las 6 cards tipo **sinergia / Conocimiento General (Optativas)** = los 6 docs del eje Conocimiento General (DM/DX), todas conectadas.
- NOTA: "Producción Artística Interdisciplinaria" e "Innovación en Diseño" y "Diseño de Futuros" NO son cards visibles; son solo `slugId` heredados que ahora usan las cards sinergia (Metodologías, Diseño Participativo, Materiales Experimentales respectivamente). No hay materias huérfanas.
- Identidad de Marca I ← "Diseño de identidad forma y significado"; Identidad de Marca II ← "Diseño de Sistemas de Marca"; Gestión de Producción ← "Producción de Diseño y Prototipos"; Prototipado de Experiencias ← "Diseño de Interfaz"; Diseño y Negocios Creativos ← "De la Idea Gráfica al Mercado".
- Cards sin docx (placeholders, esperado): Formación UDEM (×5), Prácticas Profesionales, Conocimiento General.

### Pendiente menor
- Verificado en preview (puerto 8090): 35/35 materias muestran su info; sin errores de consola.
- Si en el futuro se quiere que esto sobreviva a un cambio de nombres de card, considerar migrar `COURSE_DOCS` a Firebase `ldgd/plans` o re-keyar.

## #changed

### Materias renombradas en `index.html` + Firebase (todas verificadas en preview)

| Antes | Después | Razón |
|---|---|---|
| Concentración A · Dir. de Arte y Fotografía de Producto | Certificado · Dir. de Arte y Fotografía de Producto | Unificación de A/B → Certificado único |
| Concentración A · Dirección Visual de Marca | Certificado · Dirección Visual de Marca | Idem |
| Concentración A · Motion Design y Contenido Digital | Certificado · Animación Gráfica y Contenido Digital | UDEM rule: no anglicismos |
| Concentración B · Gestión de Proyectos Creativos | Certificado · Gestión de Proyectos Creativos | Idem |
| Concentración B · Consultoría y Estrategia de Diseño | Certificado · Inteligencia Artificial Aplicada al Diseño Visual | Sustitución por materia nueva (Escenario B) |
| Concentración B · Emprendimiento Creativo | Certificado · Diseño y Negocios Creativos | Renombrada por solicitud del director |
| Diseño Visual I: Principios y Composición | Estudio de principios y composición visual | UDEM rule: sin seriación, sin dos puntos, prefijo "Estudio" |
| Diseño Visual II: Forma, Color y Estructura | Estudio de forma, color y estructura | Idem |
| Visualización y Pensamiento de Diseño | Visualización y pensamiento de diseño | UDEM rule: solo primera mayúscula |
| Ilustración Aplicada | Ilustración aplicada | Idem |

### Estructura del Certificado (`view-certificados` en `index.html`)
- Sustituidas las 2 cards (Concentración A + B) por **1 sola card** del Certificado unificado
- Tab "Concentraciones" → "Certificado"
- CSS `.conc-a` y `.conc-b` → `.is-cert` unificado
- 6 roles de egreso ampliados (incluye IA + motion)
- `syncConcNames()` adaptado a estructura única

### Excel `LDV-2027_Bibliografia_Basica.xlsx`
- 5 hojas (Bibliografía, Resumen, Solicitud_Biblioteca, Catálogo_CRGS, Validación)
- 46 materias precargadas con sem/clave/tipo/eje
- **Bibliografía agregada para 5 materias** (ver lista #current_state)
- Dropdowns en columnas (Idioma, Tipo de fuente, Carácter, Disponibilidad, Acción)
- Formato condicional (rojo si "No disponible", verde si "Sí")
- Fórmulas de conteo en Hoja Resumen

### Plan analítico fields actualizados (DV1, DV2, Ilustración, Visualización, DI, C6 Diseño y Negocios)
- Cada uno tiene:
  - Denominación
  - Ciclo (semestre)
  - Clave `DV X NNN` (X = bloque según semestre; NNN placeholder Normatividad)
  - Fin de aprendizaje en fórmula UDEM
  - Contenido temático en bloques temáticos
  - Actividades bajo conducción
  - Actividades independientes
  - Criterios de evaluación con %
- En materias con base de profesor (DV1, DV2): contenido del profesor sin highlight + propuestas mías en **amarillo**
- En materias propuesta original (Ilustración, Visualización, IA-related): todo en **amarillo**
- En materias del 2021 actualizadas (DI): solo lo nuevo en **amarillo**, lo conservado sin highlight

### `codigo-ia.html` — Pieza interactiva inmersiva
- **6 escenas con routing GSAP**: entry → hub orbital → 5 paths
- **Hub orbital**: 5 cards en posición circular (-90°, -18°, 54°, 126°, 198°) con mouse parallax, 3 anillos concéntricos animados, toggle órbita/lista
- **Path 01 · Declarar**: formulario + preview live + copy clipboard
- **Path 02 · Wizard**: 3 frames fullscreen + verdict animado tipo "sello institucional" + handoff a Path 01
- **Path 03 · Manifiesto**: 4 frames con dots de progreso + controles
- **Path 04 · Profesores**: 4 principios + 6 criterios + 6 casos expandibles + recursos
- **Path 05 · Documento completo**: placeholder pendiente (Re-Entrega 3)
- **Audio engine** (Web Audio API): drone ambient sub-bass 80 Hz + LFO + armónicos + tick + whoosh + stamp
- **Custom cursor** con etiquetas contextuales
- **Side tabs** colapsadas para saltar entre paths
- **Texture tagline** repetida como fondo

### `PRD_Certificado_LDV.md`
- Actualizado a Versión 2.0
- Nota explicativa de Escenario B con justificación
- Opción D enriquecida con argumentación SEP
- Mapa de SLOs actualizado
- Tabla de riesgos con renglón RVOE / SEP

---

## #failed_attempts

### Audio en `codigo-ia.html` v1
- Ganancia inicial muy baja (`droneGain: 0.06`) → no audible
- **Fix aplicado:** subida a `0.18` + armónicos a `0.05` + pad a `0.025` + tick a `0.12` + whoosh a `0.14` + stamp a `0.32`

### Hub orbital cards no aparecían (v6)
- `positionOrbitCards()` corría antes de que la escena hub estuviera activa
- `rect.width = 0` → cards se quedaban en translate(0,0) apiladas
- **Fix aplicado:** `setTimeout(() => positionOrbitCards(true), 650)` después del whoosh, sincronizado con timeline GSAP

### Firebase customizations stale
- En sesiones anteriores las customizations de Firebase guardaban nombres viejos que sobrescribían el HTML
- Casos detectados: Dirección Visual de Marca quedó como "Toma de Decisiones en Diseño"; Motion Design no se actualizó a Animación Gráfica
- **Fix aplicado:** scripts `preview_eval` para sincronizar `ldgd/customizations` con los nombres nuevos

### Re-Entrega 1 del Código de IA (scroll lineal)
- Primera versión era scroll vertical lineal tipo Apple
- Director rechazó: pidió referencia pacomepertant.com con interacción orbital
- **Resolución:** rehecho completo como hub + paths con custom cursor, sound toggle, mouse parallax, view toggle

### Diseño de Información dentro de DI (Path 02 del plan analítico)
- Propuesta inicial incluyó un bloque "Diseño de información y arquitectura" en el plan de Estudio de Diseño de Interacción
- Director cuestionó: ya se cubre en Estudio de Diseño de Información I y II (sem 3-4)
- **Fix aplicado:** Opción B confirmada — bloque eliminado, integrado como sub-línea dentro de "Investigación de usuarios"; bloque "IA aplicada" renombrado a "Diseño de interacción con sistemas inteligentes" para no duplicar con IA Aplicada del Certificado

### % de sinergia con cifra "32%" inexacta
- Inicialmente se mantenía el 32% por paralelismo con el ejemplo de Moda (330 cr)
- Director cuestionó: LDV tiene 324 cr (6 menos)
- **Recálculo verificado:** 102/324 = **31.5%** (redondeable a 32%)

---

## #next_steps

### Inmediato (próxima sesión)
1. ~~**Decidir nombre del programa**~~ ✅ RESUELTO 2026-05-31 → `Diseño Visual y Negocios Creativos`. Archivos ya consistentes, sin ediciones pendientes. Ver #current_state.

### Plan analítico — 40 materias pendientes de las 46 totales
**Generados (6):**
- Estudio de principios y composición visual (sem 1)
- Visualización y pensamiento de diseño (sem 1)
- Estudio de forma, color y estructura (sem 2)
- Ilustración aplicada (sem 2)
- Estudio de Diseño de Interacción (sem 6)
- Diseño y Negocios Creativos (sem 8 · C6 Certificado)

**Pendientes (40):** Todas las demás del programa, incluyendo:
- Contexto cultural del diseño, Herramientas digitales para el diseño (sem 1)
- Tipografía I, Lenguaje y significado en el diseño (sem 2)
- Identidad de Marca I, Diseño de Información I, Fotografía para Diseño, Tipografía II, Direc. Creat. para Med. Audiovis. (sem 3)
- Diseño de Información II, Gestión de Producción, Diseño de Empaque, Dir. de Arte y Fotografía de Producto, Gestión de Proyectos Creativos (sem 4)
- Identidad de Marca II, Portafolio Profesional, Diseño de Futuros, Dirección Visual de Marca (sem 5)
- Diseño de Experiencia, Prototipado de Experiencias, Producción Artística Interdisciplinaria, Animación Gráfica y Contenido Digital (sem 6)
- Diseño de Servicios, Prácticas Profesionales, Innovación en Diseño, IA Aplicada al Diseño Visual (sem 7)
- Estudio Integral de Diseño, Estrategia de Negocios para el Diseño, PEF I (sem 8)
- PEF II (sem 9)
- 5× Formación UDEM + 5× Conocimiento General

**Estrategia eficiente:** generalizar los scripts `/tmp/generate_*_plan.py` en uno solo parametrizado por materia, y procesar por lotes pidiendo contexto a cada profesor responsable. Las que ya tienen contenido (DI, DV1, DV2 según docs del profesor) van rápido; las que son propuesta original toman más iteración.

### Bibliografía
- Completar las 40 materias restantes en el Excel
- Cuando se tenga acceso al catálogo CRGS, llenar columna "Disponible en Biblioteca" para detonar la Hoja "Solicitud_Biblioteca"
- Entregar a Biblioteca CRGS la Hoja 3 filtrada

### `codigo-ia.html` Re-Entrega 3 (pendiente)
- **Path 05 · Documento completo**: layout editorial con índice lateral fijo, lectura formal del código completo
- **PDF firmable**: botón en cierre que genera PDF al vuelo (jsPDF o html2pdf)
- **Pulido final**: ajustes responsive móvil, manejo de error del clipboard en navegadores antiguos
- **Integración con index.html**: agregar botón "Código IA" en la malla (probablemente en el header o en una tab nueva)

### Tabla comparativa Plan 2021 vs 2027
- Lista para integrar al documento SACS / institucional
- Campos llenados en sesión: Perfil de egreso, Trayectorias laborales, Principales cambios, Elementos diferenciadores, Créditos/semestres (324 / 9), % Sinergia (32% redondeado, 31.5% exacto)
- Falta: si cambia el nombre del programa, reescribir el bloque "Principales cambios" en la nueva clave argumentativa (modificación vs nuevo programa)

### Documento SACS Substantive Change
- Decidir si es **Opening a New Program** (Diseño Visual) o **Significant Modification** (Diseño Gráfico y Negocios Creativos)
- Llenar las 10 secciones del formato SACS UDEM compartido en sesión:
  1. Abstract
  2. Need + Approvals
  3. Specific Substantive Change Info
  4. Faculty
  5. Library
  6. Student Support
  7. Physical Resources
  8. Financial Support
  9. Evaluation/Assessment
  10. Attachments
- Coordinar con Benito Flores (Accreditation Liaison) — benito.flores@udem.edu.mx

### Pendientes administrativos
- Solicitar a Normatividad UDEM las **claves NNN** definitivas para cada materia nueva (sustituir `DV X NNN` por la clave asignada)
- Confirmar codes de departamento para Formación UDEM (`FU?`) y Conocimiento General (`CG?`)
- Confirmar si la bibliografía va dentro del Anexo 3 (algunas escuelas tienen variante) o por separado a Biblioteca

---

## Notas operativas

### Cómo ver la app de la malla en vivo
```bash
# Preview server config: .claude/launch.json → "ldv-2027" en puerto 8090
# Para ver la malla:        http://localhost:8090/index.html
# Para ver el Código IA:    http://localhost:8090/codigo-ia.html
# Para ver la propuesta:    http://localhost:8090/certificado-propuesta.html
```

### Firebase auth
Para overrides administrativos en `ldgd/customizations`, usar el password de admin desde el botón "Entrar" de la landing del index.html.

### Git
- Branch: `main`
- Estado de divergencia: 3 commits locales adelante, 9 remotos atrás (pendiente reconciliar antes de push)
- Último commit local: `04ab063` — Unificación de Concentraciones en un solo Certificado

### Recordatorio de reglas UDEM nombres de materias
1. Solo primera palabra con mayúscula (ej. "Estudio de principios y composición visual")
2. Sin numeración seriada (no "I", "II")
3. Sin dos puntos, paréntesis, guiones
4. Comas permitidas en listas (ej. "Estudio de forma, color y estructura")
5. Sin anglicismos salvo tecnicismos reconocidos (lean startup, brand, UX/UI sí; storytelling, moodboard reemplazar)
6. Clave formato `XX N NNN` donde XX = depto, N = bloque semestre (1=1-2, 2=3-4, 3=5-6, 4=7-8, 5=9+), NNN = consecutivo Normatividad

---

**Fin del handoff.**
