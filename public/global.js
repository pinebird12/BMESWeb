// Setting current on the navbar

let navLinks = Array.from(document.querySelectorAll('.navbar > a'));

const dropLinks = Array.from(document.querySelectorAll('.dropdown-content > a'));

navLinks = navLinks.concat(dropLinks);

console.log(navLinks);

let currentLink = navLinks.find(
  (a) => a.host === location.host && a.pathname === location.pathname,
);

if (currentLink) {
  currentLink.classList.add('current')
}

console.log(currentLink);

// if (currentLink) {
//   currentLink.classList.add('current');
// };
