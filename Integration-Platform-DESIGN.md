---
version: "alpha"
name: "Integration Platform"
description: "Integration Platform Login Section is designed for authenticating users through a focused access flow. Key features include reusable structure, responsive behavior, and production-ready presentation. It is suitable for authentication screens in web products."
colors:
  primary: "#A3E635"
  secondary: "#BEF264"
  tertiary: "#84CC16"
  neutral: "#0A0A0A"
  background: "#0A0A0A"
  surface: "#A3E635"
  text-primary: "#A3A3A3"
  text-secondary: "#FFFFFF"
  border: "#FFFFFF"
  accent: "#A3E635"
typography:
  display-lg:
    fontFamily: "System Font"
    fontSize: "60px"
    fontWeight: 400
    lineHeight: "60px"
    letterSpacing: "-0.025em"
  body-md:
    fontFamily: "System Font"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "24px"
  label-md:
    fontFamily: "System Font"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: "20px"
    letterSpacing: "0.025em"
spacing:
  base: "4px"
  sm: "1px"
  md: "4px"
  lg: "12px"
  xl: "15px"
  gap: "6px"
  section-padding: "128px"
---

## Overview

- **Composition cues:**
  - Layout: Flex
  - Content Width: Full Bleed
  - Framing: Glassy
  - Grid: Minimal

## Colors

The color system uses dark mode with #A3E635 as the main accent and #0A0A0A as the neutral foundation.

- **Primary (#A3E635):** Main accent and emphasis color.
- **Secondary (#BEF264):** Supporting accent for secondary emphasis.
- **Tertiary (#84CC16):** Reserved accent for supporting contrast moments.
- **Neutral (#0A0A0A):** Neutral foundation for backgrounds, surfaces, and supporting chrome.

- **Usage:** Background: #0A0A0A; Surface: #A3E635; Text Primary: #A3A3A3; Text Secondary: #FFFFFF; Border: #FFFFFF; Accent: #A3E635

- **Gradients:** bg-gradient-to-b from-white/20 to-white/0, bg-gradient-to-b from-transparent to-transparent via-white/10, bg-gradient-to-b from-lime-400/60 to-lime-400/0

## Typography

Typography relies on System Font across display, body, and utility text.

- **Display (`display-lg`):** System Font, 60px, weight 400, line-height 60px, letter-spacing -0.025em.
- **Body (`body-md`):** System Font, 16px, weight 400, line-height 24px.
- **Labels (`label-md`):** System Font, 14px, weight 400, line-height 20px, letter-spacing 0.025em.

## Layout

Layout follows a flex composition with reusable spacing tokens. Preserve the flex, full bleed structural frame before changing ornament or component styling. Use 4px as the base rhythm and let larger gaps step up from that cadence instead of introducing unrelated spacing values.

Treat the page as a flex / full bleed composition, and keep that framing stable when adding or remixing sections.

- **Layout type:** Flex
- **Content width:** Full Bleed
- **Base unit:** 4px
- **Scale:** 1px, 4px, 12px, 15px, 16px, 24px, 26px, 32px
- **Section padding:** 128px
- **Gaps:** 6px, 10px, 32px

## Elevation & Depth

Depth is communicated through glass, border contrast, and reusable shadow or blur treatments. Keep those recipes consistent across hero panels, cards, and controls so the page reads as one material system.

Surfaces should read as glass first, with borders, shadows, and blur only reinforcing that material choice.

- **Surface style:** Glass
- **Borders:** 1px #FFFFFF; 1px #262626
- **Shadows:** rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.25) 0px 25px 50px -12px; rgb(255, 255, 255) 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 0px 0px 0px; rgb(255, 255, 255) 0px 0px 0px 0px inset, rgba(163, 230, 53, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px
- **Blur:** 4px, 12px

### Techniques
- **Gradient border shell:** Use a thin gradient border shell around the main card. Wrap the surface in an outer shell with 0px padding and a 0px radius. Drive the shell with none so the edge reads like premium depth instead of a flat stroke. Keep the actual stroke understated so the gradient shell remains the hero edge treatment. Inset the real content surface inside the wrapper with a slightly smaller radius so the gradient only appears as a hairline frame.

## Shapes

Shapes rely on a tight radius system anchored by 12px and scaled across cards, buttons, and supporting surfaces. Icon geometry should stay compatible with that soft-to-controlled silhouette.

Use the radius family intentionally: larger surfaces can open up, but controls and badges should stay within the same rounded DNA instead of inventing sharper or pill-only exceptions.

- **Corner radii:** 12px, 16px, 9999px
- **Icon treatment:** Linear
- **Icon sets:** Solar

## Components

Component styling should inherit the shared button, icon, spacing, and surface rules instead of inventing one-off treatments. Favor a small family of repeatable patterns for actions, content containers, and fields.

### Iconography
- **Treatment:** Linear.
- **Sets:** Solar.

## Do's and Don'ts

Use these constraints to keep future generations aligned with the current system instead of drifting into adjacent styles.

### Do
- Do use the primary palette as the main accent for emphasis and action states.
- Do keep spacing aligned to the detected 4px rhythm.
- Do reuse the Glass surface treatment consistently across cards and controls.
- Do keep corner radii within the detected 12px, 16px, 9999px family.

### Don't
- Don't introduce extra accent colors outside the core palette roles unless the page needs a new semantic state.
- Don't mix unrelated shadow or blur recipes that break the current depth system.
- Don't exceed the detected moderate motion intensity without a deliberate reason.

## Motion

Motion feels controlled and interface-led across text, layout, and section transitions. Timing clusters around 500ms and 150ms. Easing favors ease and cubic-bezier(0.4. Hover behavior focuses on transform and text changes. Scroll choreography uses GSAP ScrollTrigger and Parallax for section reveals and pacing.

**Motion Level:** moderate

**Durations:** 500ms, 150ms

**Easings:** ease, cubic-bezier(0.4, 0, 0.2, 1)

**Hover Patterns:** transform, text

**Scroll Patterns:** gsap-scrolltrigger, parallax

## WebGL

Reconstruct the graphics as a wide scene band using webgl, renderer, alpha, antialias, dpr clamp. The effect should read as technical, meditative, and atmospheric: dot-matrix particle field with black and sparse spacing. Build it from dot particles + soft depth fade so the effect reads clearly. Animate it as slow breathing pulse. Interaction can react to the pointer, but only as a subtle drift. Preserve reduced motion + dom fallback.

**Id:** webgl

**Label:** WebGL

**Stack:** ThreeJS, WebGL

**Insights:**
  - **Scene:**
    - **Value:** Wide scene band
  - **Effect:**
    - **Value:** Dot-matrix particle field
  - **Primitives:**
    - **Value:** Dot particles + soft depth fade
  - **Motion:**
    - **Value:** Slow breathing pulse
  - **Interaction:**
    - **Value:** Pointer-reactive drift
  - **Render:**
    - **Value:** WebGL, Renderer, alpha, antialias, DPR clamp

**Techniques:** Dot matrix, Breathing pulse, Pointer parallax, DOM fallback

**Code Evidence:**
  - **HTML reference:**
    - **Language:** html
    - **Snippet:**
      ```html
      <!-- WebGL Canvas replaces SVG -->
      <canvas id="webgl-canvas" class="absolute inset-0 w-full h-full pointer-events-none z-0"></canvas>

      <!-- Top Row Nodes (Absolute positioning to match logic coordinates 16.6%, 30.0%, 43.3%, 56.6%, 70.0%, 83.3%) -->
      ```
  - **JS reference:**
    - **Language:** html
    - **Snippet:**
      ```html
      <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
      ```

## ThreeJS

Reconstruct the Three.js layer as a wide scene band with layered spatial depth that feels volumetric and technical. Use alpha, antialias, dpr clamp renderer settings, orthographic projection, sphere + custom buffer geometry geometry, meshbasicmaterial materials, and ambient + key + rim lighting. Motion should read as timeline-led reveals, with reduced motion + non-3d fallback.

**Id:** threejs

**Label:** ThreeJS

**Stack:** ThreeJS, WebGL

**Insights:**
  - **Scene:**
    - **Value:** Wide scene band with layered spatial depth
  - **Render:**
    - **Value:** alpha, antialias, DPR clamp
  - **Camera:**
    - **Value:** Orthographic projection
  - **Lighting:**
    - **Value:** ambient + key + rim
  - **Materials:**
    - **Value:** MeshBasicMaterial
  - **Geometry:**
    - **Value:** sphere + custom buffer geometry
  - **Motion:**
    - **Value:** Timeline-led reveals

**Techniques:** Particle depth, Timeline beats, alpha, antialias, DPR clamp, Reduced motion + non-3D fallback

**Code Evidence:**
  - **HTML reference:**
    - **Language:** html
    - **Snippet:**
      ```html
      <!-- WebGL Canvas replaces SVG -->
      <canvas id="webgl-canvas" class="absolute inset-0 w-full h-full pointer-events-none z-0"></canvas>

      <!-- Top Row Nodes (Absolute positioning to match logic coordinates 16.6%, 30.0%, 43.3%, 56.6%, 70.0%, 83.3%) -->
      ```
  - **JS reference:**
    - **Language:** html
    - **Snippet:**
      ```html
      <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
      ```
