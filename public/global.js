// Setting current on the navbar

let navLinks = Array.from(document.querySelectorAll('.navbar > a'));

const dropLinks = Array.from(document.querySelectorAll('.dropdown-content > a'));
console.log(dropLinks);
navLinks = navLinks.concat(dropLinks);


let currentLink = navLinks.find(
  (a) => a.host === location.host && a.pathname === location.pathname,
);

if (currentLink) {
  currentLink.classList.add('current')
}

if (dropLinks.find(
  (a) => a.host === location.host && a.pathname === location.pathname,
)) {
  const dropdown = currentLink.parentElement.parentElement;
  dropdown.classList.add('current');
}
