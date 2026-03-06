<template>
  <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar ftco-navbar-light site-navbar-target" id="ftco-navbar">
    <div class="container">
      <a class="navbar-brand" href="/">Clark</a>
      <button class="navbar-toggler js-fh5co-nav-toggle fh5co-nav-toggle" type="button" @click="toggleMenu" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="oi oi-menu"></span> Menu
      </button>

      <div class="collapse navbar-collapse" :class="{ 'show': isMenuOpen }" id="ftco-nav">
        <ul class="navbar-nav nav ml-auto">
          <li class="nav-item"><a href="#home-section" class="nav-link" @click="handleNavClick"><span>Home</span></a></li>
          <li class="nav-item"><a href="#about-section" class="nav-link" @click="handleNavClick"><span>About</span></a></li>
          <li class="nav-item"><a href="#resume-section" class="nav-link" @click="handleNavClick"><span>Resume</span></a></li>
          <li class="nav-item"><a href="#services-section" class="nav-link" @click="handleNavClick"><span>Services</span></a></li>
          <li class="nav-item"><a href="#skills-section" class="nav-link" @click="handleNavClick"><span>Skills</span></a></li>
          <li class="nav-item"><a href="#projects-section" class="nav-link" @click="handleNavClick"><span>Projects</span></a></li>
          <li class="nav-item"><a href="#blog-section" class="nav-link" @click="handleNavClick"><span>My Blog</span></a></li>
          <li class="nav-item"><a href="#contact-section" class="nav-link" @click="handleNavClick"><span>Contact</span></a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const isMenuOpen = ref(false);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const handleNavClick = (e) => {
  e.preventDefault();
  const targetId = e.currentTarget.getAttribute('href');
  const targetElement = document.querySelector(targetId);
  if (targetElement) {
    const offset = 70;
    const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - offset;
    window.scrollTo({
      top: targetPosition,
      behavior: 'smooth'
    });
  }
  isMenuOpen.value = false;
};

const handleScroll = () => {
  const navbar = document.querySelector('.ftco_navbar');
  if (window.scrollY > 150) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
    navbar.classList.remove('sleep');
  }

  if (window.scrollY > 350) {
    navbar.classList.add('awake');
  } else {
    if (navbar.classList.contains('awake')) {
      navbar.classList.remove('awake');
      navbar.classList.add('sleep');
    }
  }
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>
