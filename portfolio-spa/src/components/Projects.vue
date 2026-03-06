<template>
  <section class="ftco-section ftco-project" id="projects-section">
    <div class="container">
      <div class="row justify-content-center pb-5">
        <div class="col-md-12 heading-section text-center" data-aos="fade-up" data-aos-duration="1000">
          <h1 class="big big-2">Projects</h1>
          <h2 class="mb-4">Our Projects</h2>
          <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia</p>
        </div>
      </div>
      <div class="row">
        <div class="col-md-4" data-aos="fade-up" data-aos-delay="0">
          <div class="project img d-flex justify-content-center align-items-center" :style="{ backgroundImage: `url(${project4})` }">
            <div class="overlay"></div>
            <div class="text text-center p-4">
              <h3><a href="#">Branding &amp; Illustration Design</a></h3>
              <span>Web Design</span>
            </div>
          </div>
        </div>
        <div class="col-md-8" data-aos="fade-up" data-aos-delay="100">
          <div class="project img d-flex justify-content-center align-items-center" :style="{ backgroundImage: `url(${project5})` }">
            <div class="overlay"></div>
            <div class="text text-center p-4">
              <h3><a href="#">Branding &amp; Illustration Design</a></h3>
              <span>Web Design</span>
            </div>
          </div>
        </div>

        <div class="col-md-8">
          <div class="project img d-flex justify-content-center align-items-center" 
               style="margin-bottom: 30px;"
               :style="{ backgroundImage: `url(${project1})` }"
               data-aos="fade-up" data-aos-delay="0">
            <div class="overlay"></div>
            <div class="text text-center p-4">
              <h3><a href="#">Branding &amp; Illustration Design</a></h3>
              <span>Web Design</span>
            </div>
          </div>

          <div class="project img d-flex justify-content-center align-items-center" 
               :style="{ backgroundImage: `url(${project6})` }"
               data-aos="fade-up" data-aos-delay="100">
            <div class="overlay"></div>
            <div class="text text-center p-4">
              <h3><a href="#">Branding &amp; Illustration Design</a></h3>
              <span>Web Design</span>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="row">
            <div class="col-md-12" data-aos="fade-up" data-aos-delay="200">
              <div class="project img d-flex justify-content-center align-items-center" :style="{ backgroundImage: `url(${project2})` }">
                <div class="overlay"></div>
                <div class="text text-center p-4">
                  <h3><a href="#">Branding &amp; Illustration Design</a></h3>
                  <span>Web Design</span>
                </div>
              </div>
            </div>
            <div class="col-md-12" data-aos="fade-up" data-aos-delay="300" style="margin-top: 30px;">
              <div class="project img d-flex justify-content-center align-items-center" :style="{ backgroundImage: `url(${project3})` }">
                <div class="overlay"></div>
                <div class="text text-center p-4">
                  <h3><a href="#">Branding &amp; Illustration Design</a></h3>
                  <span>Web Design</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import project1 from '@/assets/images/project-1.jpg';
import project2 from '@/assets/images/project-2.jpg';
import project3 from '@/assets/images/project-3.jpg';
import project4 from '@/assets/images/project-4.jpg';
import project5 from '@/assets/images/project-5.jpg';
import project6 from '@/assets/images/project-6.jpg';
</script>
