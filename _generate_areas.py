"""Generate Nassau County location pages for Y&M website."""
import os

LOCATIONS = [
    {
        "slug": "hempstead",
        "name": "Hempstead",
        "zips": "11550, 11551, 11553, 11554",
        "meta_title": "Fire Extinguisher Inspection in Hempstead, NY — NFPA 10 Certified | Y&M",
        "meta_desc": "Certified fire extinguisher inspection, recharge, and service in Hempstead, NY. Restaurants, multi-family, retail, and houses of worship. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Hempstead NY, fire extinguisher service Hempstead, NFPA 10 Hempstead, Hempstead fire safety",
        "subheading": "Local extinguisher service for the largest village in Nassau County.",
        "intro": "From Fulton Avenue to Hempstead Turnpike, we keep Hempstead&rsquo;s restaurants, multi-family buildings, retail storefronts, and houses of worship NFPA&nbsp;10 compliant &mdash; with certified inspections, dated tags, and a real local point of contact.",
        "context": "The Village of Hempstead is the largest village in New York State and the seat of the Town of Hempstead. Anchored by Hofstra University and Nassau Community College, it has a dense commercial corridor along Fulton Avenue and Main Street, plus retail and auto-service along Hempstead Turnpike and Peninsula Boulevard. The mix of student housing, multi-family residential, places of worship, and small storefront commerce makes inspection coverage especially varied here.",
        "properties": "We commonly service Hempstead restaurants and food trucks (Class&nbsp;K for fryers, ABC for dining areas), multi-family residential buildings near the Hofstra campus (common-area extinguishers, mechanical rooms, laundry rooms), retail and convenience stores along Fulton Avenue, auto-service shops, and the village&rsquo;s many churches and community centers.",
        "nearby": "Uniondale, West Hempstead, Garden City, Roosevelt, Freeport",
    },
    {
        "slug": "garden-city",
        "name": "Garden City",
        "zips": "11530, 11531",
        "meta_title": "Fire Extinguisher Inspection in Garden City, NY — Roosevelt Field Area | Y&M",
        "meta_desc": "Certified fire extinguisher service in Garden City, NY. Roosevelt Field, Franklin Avenue, hotels, and professional offices. NFPA 10 compliant. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Garden City NY, Roosevelt Field fire extinguisher, Garden City NFPA 10, Franklin Avenue fire safety",
        "subheading": "Upscale commercial and retail extinguisher service in Garden City.",
        "intro": "Roosevelt Field, Franklin Avenue, the Garden City Hotel, and a dense corridor of professional offices &mdash; we keep Garden City&rsquo;s commercial properties NFPA&nbsp;10 compliant with certified annual inspections and clear documentation.",
        "context": "Garden City is one of Nassau County&rsquo;s most active commercial centers, home to Roosevelt Field &mdash; among the largest shopping malls in the United States &mdash; plus Adelphi University, the Garden City Hotel, and the Cradle of Aviation Museum. Franklin Avenue&rsquo;s downtown spine and the Old Country Road retail belt drive a heavy mix of mall tenants, sit-down restaurants, hotel and hospitality, and Class&nbsp;A professional offices.",
        "properties": "We service Garden City retailers and restaurant tenants inside Roosevelt Field, fine-dining and casual restaurants along Seventh Street and Franklin Avenue (heavy Class&nbsp;K demand), professional, medical, and law-firm offices (CO&#8322; for electronics and electrical), the Garden City Hotel and surrounding hospitality, and Adelphi-area multi-family and academic buildings.",
        "nearby": "Mineola, Westbury, Hempstead, Franklin Square, Carle Place",
    },
    {
        "slug": "mineola",
        "name": "Mineola",
        "zips": "11501",
        "meta_title": "Fire Extinguisher Inspection in Mineola, NY — Courthouse, Hospital & Downtown | Y&M",
        "meta_desc": "Certified fire extinguisher service in Mineola, NY. Nassau County Courthouse, NYU Langone Long Island Hospital, legal and medical offices. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Mineola NY, Mineola NFPA 10, Mineola medical office fire safety, Mineola fire extinguisher service",
        "subheading": "Fire extinguisher service for Nassau County&rsquo;s seat &mdash; courthouse, hospital, and downtown.",
        "intro": "Mineola anchors the Nassau County government district, the NYU Langone Long Island Hospital campus, and a dense legal and medical professional corridor. We keep them all current on NFPA&nbsp;10.",
        "context": "Mineola is the seat of Nassau County. It hosts the County Courthouse complex, NYU Langone Long Island Hospital (formerly Winthrop), Nassau University Medical Center, and a dense cluster of law firms, medical groups, and professional offices in between. Old Country Road and Mineola Boulevard mix professional services with retail, restaurants, and multi-family residential.",
        "properties": "Mineola work skews professional and medical: law and accounting offices (CO&#8322; where electronics and electrical risk dominate), medical and dental practices (clean-agent priorities), restaurants along Mineola Boulevard and Jericho Turnpike (Class&nbsp;K), and the multi-family residential corridors close to the LIRR station.",
        "nearby": "Garden City, Williston Park, Carle Place, Westbury, Albertson, New Hyde Park",
    },
    {
        "slug": "hicksville",
        "name": "Hicksville",
        "zips": "11801, 11802",
        "meta_title": "Fire Extinguisher Inspection in Hicksville, NY — Broadway Commercial Corridor | Y&M",
        "meta_desc": "Certified fire extinguisher service in Hicksville, NY. South Broadway restaurants, retail, and auto-service. NFPA 10 compliant. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Hicksville NY, Hicksville Broadway fire safety, Hicksville restaurant Class K, Hicksville NFPA 10",
        "subheading": "Local extinguisher service across Hicksville&rsquo;s Broadway commercial corridor.",
        "intro": "From the South Broadway commercial district to Hicksville Plaza and Mid-Island Plaza, we keep Hicksville&rsquo;s retail, restaurants, and auto-service properties NFPA&nbsp;10 compliant year after year.",
        "context": "Hicksville is one of the busiest commercial centers in the Town of Oyster Bay, anchored by the Hicksville LIRR &mdash; one of the busiest commuter stations on Long Island &mdash; and a dense Broadway corridor that runs the length of the hamlet. The South Broadway district has become a recognized Indian, Pakistani, and Bangladeshi commercial cluster, with hundreds of restaurants, grocers, and storefront businesses. Add in Mid-Island Plaza, Old Country Road retail, and a strong auto-service presence, and the inspection workload is varied and constant.",
        "properties": "Hicksville&rsquo;s commercial mix means heavy work across all extinguisher classes: ABC for the dense storefront retail and grocery, Class&nbsp;K for the major restaurant cluster along South Broadway, CO&#8322; for the offices and electronics retail near the LIRR, and higher-rated extra-hazard units for auto-service shops and small warehouses.",
        "nearby": "Bethpage, Plainview, Jericho, Levittown, Westbury, Old Bethpage",
    },
    {
        "slug": "levittown",
        "name": "Levittown",
        "zips": "11756",
        "meta_title": "Fire Extinguisher Inspection in Levittown, NY — Local Service | Y&M",
        "meta_desc": "Certified fire extinguisher service for Levittown small businesses, restaurants, gas stations, and houses of worship. NFPA 10 compliant. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Levittown NY, Levittown NFPA 10, Hempstead Turnpike fire safety, Levittown fire extinguisher service",
        "subheading": "Local extinguisher service for Levittown&rsquo;s small businesses and houses of worship.",
        "intro": "From Hempstead Turnpike to Wantagh Avenue, we keep Levittown&rsquo;s restaurants, storefronts, gas stations, and community spaces compliant &mdash; without the big-vendor markup.",
        "context": "Levittown is the original American post-war planned suburb. While primarily residential, the hamlet&rsquo;s commercial spine runs along Hempstead Turnpike and Wantagh Avenue, with strip retail, gas stations, auto shops, restaurants, and the houses of worship and community centers that anchor neighborhood life.",
        "properties": "Levittown work tends to be smaller-scale per site but high frequency: pizzerias and casual restaurants (ABC plus Class&nbsp;K where there&rsquo;s a fryer), strip retail and convenience stores, gas stations and auto repair (extra-hazard ratings), and the elementary schools, religious schools, and community spaces that need annual inspection without disrupting operations.",
        "nearby": "Hicksville, East Meadow, Wantagh, Seaford, Bethpage",
    },
    {
        "slug": "freeport",
        "name": "Freeport",
        "zips": "11520, 11521",
        "meta_title": "Fire Extinguisher Inspection in Freeport, NY — Nautical Mile & Main Street | Y&M",
        "meta_desc": "Certified fire extinguisher service in Freeport, NY. Nautical Mile restaurants, marinas, and Main Street retail. Class K specialists. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Freeport NY, Nautical Mile fire safety, Freeport restaurant Class K, Freeport marina fire extinguisher",
        "subheading": "Restaurant, marina, and Main Street extinguisher service in Freeport.",
        "intro": "From the Nautical Mile on Woodcleft Avenue to Sunrise Highway and Main Street, Freeport&rsquo;s restaurants, marinas, and retail keep us busy year-round.",
        "context": "Freeport&rsquo;s identity is its waterfront. The Nautical Mile along Woodcleft Avenue is one of Long Island&rsquo;s most recognized restaurant rows &mdash; seafood houses, bars, and marinas lining the canals &mdash; with a peak season that demands all extinguishers be tagged and ready before the warmer months. Beyond the waterfront, Freeport&rsquo;s Main Street and Sunrise Highway corridors carry general retail, restaurants, and a strong multi-family residential surround.",
        "properties": "Freeport&rsquo;s restaurant density drives heavy Class&nbsp;K demand. We service Nautical Mile seafood and bar venues (Class&nbsp;K for fryers, ABC for dining and back-of-house, extra-hazard for fuel storage near marinas), Main Street retail and restaurants, marina-adjacent service businesses, and the multi-family residential buildings that sit between the canals and the village.",
        "nearby": "Baldwin, Merrick, Roosevelt, Bellmore, Oceanside",
    },
    {
        "slug": "long-beach",
        "name": "Long Beach",
        "zips": "11561",
        "meta_title": "Fire Extinguisher Inspection in Long Beach, NY — Boardwalk & Park Avenue | Y&M",
        "meta_desc": "Certified fire extinguisher service in Long Beach, NY. Boardwalk hotels, restaurants on West Beech & Park Avenue, multi-family condos. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Long Beach NY, Long Beach hotel fire safety, Long Beach restaurant Class K, boardwalk fire extinguisher",
        "subheading": "Boardwalk, beachfront, and Park Avenue extinguisher service in Long Beach.",
        "intro": "Hotels, beachfront restaurants, multi-family condos, and the businesses along West Beech and Park Avenue &mdash; we keep Long Beach NFPA&nbsp;10 compliant in a salt-air environment that punishes equipment.",
        "context": "Long Beach is a barrier-island city with 2.2 miles of boardwalk, oceanfront hotels, and a dense year-round restaurant and bar scene clustered along West Beech Street, Park Avenue, and East Park Avenue. Hospitality and food service dominate, alongside a heavy multi-family residential footprint of co-ops and condos that line the boardwalk and side streets.",
        "properties": "Long Beach work centers on hospitality (hotels along the boardwalk and across the city), Class&nbsp;K-heavy restaurants and bars on West Beech and Park Avenue, multi-family residential buildings (common areas, mechanical rooms, garages, laundry rooms), and beach concessions and retail. The salt-air corrosion problem is real here &mdash; extinguisher shells deteriorate faster than inland, which makes annual inspection and timely hydrostatic testing especially important.",
        "nearby": "Lido Beach, Island Park, Atlantic Beach, Point Lookout, East Atlantic Beach",
    },
    {
        "slug": "glen-cove",
        "name": "Glen Cove",
        "zips": "11542",
        "meta_title": "Fire Extinguisher Inspection in Glen Cove, NY — Downtown & Hospital | Y&M",
        "meta_desc": "Certified fire extinguisher service in Glen Cove, NY. Downtown, Glen Cove Hospital, waterfront industrial. NFPA 10 compliant. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Glen Cove NY, Glen Cove hospital fire safety, Glen Cove NFPA 10, Glen Cove fire extinguisher service",
        "subheading": "Downtown, hospital, and waterfront extinguisher service for Glen Cove.",
        "intro": "Glen Cove is Nassau County&rsquo;s smallest city &mdash; but its mix of downtown, healthcare, and industrial waterfront keeps the inspection schedule full.",
        "context": "Glen Cove is a small North Shore city with a downtown along School Street and Glen Street, plus Glen Cove Hospital, a working industrial waterfront, and the historic Gold Coast estates of the surrounding Locust Valley and Lattingtown area. The commercial mix runs from boutique downtown retail and restaurants to light-industrial sites along Garvies Point and the harbor.",
        "properties": "We service Glen Cove&rsquo;s downtown restaurants and bars (Class&nbsp;K plus ABC), boutique retail, the hospital and surrounding medical offices (CO&#8322; where appropriate), light-industrial and warehouse sites on the waterfront (higher-rated ABC, extra-hazard), and multi-family residential through the city&rsquo;s older neighborhoods.",
        "nearby": "Sea Cliff, Locust Valley, Old Brookville, Lattingtown, Bayville",
    },
    {
        "slug": "great-neck",
        "name": "Great Neck",
        "zips": "11020, 11021, 11022, 11023, 11024, 11026",
        "meta_title": "Fire Extinguisher Inspection in Great Neck, NY — Middle Neck Road | Y&M",
        "meta_desc": "Certified fire extinguisher service across the Great Neck peninsula. Middle Neck Road restaurants, retail, professional offices. NFPA 10 compliant. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Great Neck NY, Great Neck restaurant fire safety, Middle Neck Road fire extinguisher, Great Neck NFPA 10",
        "subheading": "Middle Neck Road, downtown Great Neck, and the peninsula&rsquo;s many small businesses.",
        "intro": "From Middle Neck Road&rsquo;s storefronts to the office buildings near the Great Neck LIRR, we keep the peninsula&rsquo;s restaurants, retail, and professional offices NFPA&nbsp;10 compliant.",
        "context": "The Great Neck peninsula is made up of nine villages &mdash; Great Neck, Great Neck Estates, Kensington, Russell Gardens, Saddle Rock, Great Neck Plaza, Lake Success, and the rest &mdash; clustered around the Great Neck LIRR. Middle Neck Road is the commercial spine, with kosher and Persian-Iranian restaurants, jewelers, dry cleaners, professional offices, and a tight small-business community. North of Northern Boulevard, the commercial character shifts toward larger office buildings and retail along the LIE service road.",
        "properties": "Great Neck&rsquo;s storefront density drives heavy ABC and Class&nbsp;K demand. We service downtown restaurants &mdash; including the strong Persian-Iranian and kosher restaurant cluster &mdash; retail along Middle Neck Road, professional offices (legal, medical, financial, jewelers), dry cleaners, and the multi-family residential buildings on the peninsula&rsquo;s side streets.",
        "nearby": "Manhasset, Kings Point, Roslyn, Port Washington, Lake Success",
    },
    {
        "slug": "port-washington",
        "name": "Port Washington",
        "zips": "11050, 11051, 11052, 11053, 11054",
        "meta_title": "Fire Extinguisher Inspection in Port Washington, NY — Main Street & Harbor | Y&M",
        "meta_desc": "Certified fire extinguisher service in Port Washington, NY. Main Street restaurants, harbor marinas, professional offices. NFPA 10 compliant. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Port Washington NY, Port Washington Main Street fire safety, Port Washington marina fire extinguisher",
        "subheading": "Main Street, harbor, and marina-area extinguisher service in Port Washington.",
        "intro": "From downtown Main Street&rsquo;s restaurant row to Manhasset Bay&rsquo;s marinas, we keep Port Washington&rsquo;s commercial properties NFPA&nbsp;10 compliant.",
        "context": "Port Washington is a North Shore peninsula on Manhasset Bay, with a Main Street commercial corridor that fills with year-round restaurants and retail, plus a working harbor lined with yacht clubs, marinas, and waterfront restaurants. Shore Road and Plandome Road extend the commercial footprint, and the surrounding residential is dense multi-family near the LIRR plus single-family throughout the peninsula.",
        "properties": "Restaurants drive a lot of Port Washington work &mdash; Class&nbsp;K for the Main Street and Shore Road cluster, ABC for dining areas, retail, and back-of-house. We also service marina-related operations and yacht-club commercial buildings (where flammable-liquid hazard ratings come into play), professional offices, and the multi-family residential buildings near the LIRR.",
        "nearby": "Sands Point, Manhasset, Roslyn, Glen Head, Greenvale",
    },
    {
        "slug": "westbury",
        "name": "Westbury",
        "zips": "11590, 11592, 11593, 11595",
        "meta_title": "Fire Extinguisher Inspection in Westbury, NY — Auto Row & Old Country Road | Y&M",
        "meta_desc": "Certified fire extinguisher service in Westbury, NY. Auto dealerships, Old Country Road, Post Avenue retail, NYCB Theatre. NFPA 10 compliant. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Westbury NY, auto dealership fire extinguisher, Old Country Road NFPA 10, Westbury fire safety",
        "subheading": "Auto Row, Old Country Road, and the Westbury commercial corridor.",
        "intro": "Old Country Road&rsquo;s car-dealership row, Post Avenue retail, NYCB Theatre at Westbury &mdash; we know the inspection requirements that come with every one of these property types.",
        "context": "Westbury is best known commercially for Old Country Road &mdash; Long Island&rsquo;s auto dealership row &mdash; one of the densest concentrations of new and used car dealerships in the metro region. Beyond Auto Row, Westbury has Post Avenue downtown, the historic NYCB Theatre at Westbury (Westbury Music Fair), the Mall at the Source site, and a strong industrial and warehouse footprint between Brush Hollow Road and the LIRR tracks.",
        "properties": "Auto dealerships have specific NFPA&nbsp;10 obligations that catch a lot of operators off guard &mdash; service-bay coverage by hazard rating, paint-booth area extinguishers, parts-storage protection, and customer-area ABC. We handle all of it. Plus Post Avenue restaurants and retail (Class&nbsp;K and ABC), Brush Hollow industrial and warehouse sites (extra-hazard), and event-venue inspection for theatres and banquet halls.",
        "nearby": "Carle Place, Hicksville, Garden City, Mineola, Salisbury, Old Westbury",
    },
    {
        "slug": "massapequa",
        "name": "Massapequa",
        "zips": "11758, 11762",
        "meta_title": "Fire Extinguisher Inspection in Massapequa, NY — Sunrise Highway | Y&M",
        "meta_desc": "Certified fire extinguisher service in Massapequa, NY. Sunrise Highway retail, Park Boulevard restaurants, gas stations, auto-service. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Massapequa NY, Sunrise Highway fire safety, Massapequa restaurant Class K, Park Boulevard fire extinguisher",
        "subheading": "Sunrise Highway, Park Boulevard, and South Shore Massapequa commercial service.",
        "intro": "From the Sunrise Highway commercial corridor to Park Boulevard&rsquo;s restaurants, we keep Massapequa&rsquo;s retail, dining, and offices NFPA&nbsp;10 compliant.",
        "context": "Massapequa stretches along the Sunrise Highway corridor on the South Shore. The hamlet and its neighbors &mdash; Massapequa Park, North Massapequa, East Massapequa &mdash; share a commercial spine that runs Sunrise from west to east, with Merrick Road as the secondary corridor and Park Boulevard as the local restaurant heart. The commercial mix is solidly suburban: strip retail, restaurants and pizzerias, gyms, professional offices, gas stations, and auto.",
        "properties": "Massapequa work is mostly small- to mid-scale commercial: ABC for retail and offices, Class&nbsp;K for the strong pizzeria and Italian restaurant cluster around Park Boulevard, extra-hazard for gas stations and auto-service, and CO&#8322; for the medical and dental offices that line the corridor.",
        "nearby": "Seaford, Amityville, Farmingdale, Wantagh, North Massapequa, Massapequa Park",
    },
    {
        "slug": "syosset",
        "name": "Syosset",
        "zips": "11791, 11773",
        "meta_title": "Fire Extinguisher Inspection in Syosset, NY — Jericho Turnpike & Downtown | Y&M",
        "meta_desc": "Certified fire extinguisher service in Syosset, NY. Jericho Turnpike retail, downtown restaurants, medical offices, Syosset Hospital. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Syosset NY, Jericho Turnpike fire safety, Syosset medical office fire extinguisher, Syosset NFPA 10",
        "subheading": "Jericho Turnpike, downtown Syosset, and the North Shore commercial corridor.",
        "intro": "From the Jericho Turnpike retail belt to downtown Syosset&rsquo;s restaurants and offices, we cover the North Shore&rsquo;s busy commercial center.",
        "context": "Syosset is a North Shore hamlet in the Town of Oyster Bay with a commercial heart at the intersection of Jericho Turnpike and Berry Hill Road. Northwoods Center, Syosset Town Center, and the Jackson Avenue downtown spine combine into a dense mix of restaurants, retail, and professional services. Syosset is also notable for its medical and dental concentration, anchored by Northwell&rsquo;s Syosset Hospital.",
        "properties": "Syosset&rsquo;s mix skews professional and medical: dental and medical offices (clean-agent priorities, CO&#8322;), professional and financial services, plus the active restaurant scene along Jackson Avenue and inside the major centers (Class&nbsp;K for full-service kitchens, ABC for caf&eacute;s and quick-service). Multi-family residential and the school district&rsquo;s facilities round out the regular workload.",
        "nearby": "Woodbury, Jericho, Hicksville, East Norwich, Oyster Bay Cove, Plainview",
    },
    {
        "slug": "valley-stream",
        "name": "Valley Stream",
        "zips": "11580, 11581, 11582",
        "meta_title": "Fire Extinguisher Inspection in Valley Stream, NY — Green Acres Mall | Y&M",
        "meta_desc": "Certified fire extinguisher service in Valley Stream, NY. Green Acres Mall, Sunrise Highway retail, Rockaway Avenue restaurants. NFPA 10 compliant. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Valley Stream NY, Green Acres Mall fire safety, Sunrise Highway fire extinguisher, Rockaway Avenue NFPA 10",
        "subheading": "Green Acres Mall, Sunrise Highway retail, and downtown Valley Stream.",
        "intro": "Green Acres Mall, Sunrise Highway, and Rockaway Avenue &mdash; we cover one of the densest retail and restaurant footprints on the South Shore.",
        "context": "Valley Stream is anchored commercially by Green Acres Mall &mdash; one of the largest enclosed shopping malls on Long Island &mdash; plus a long Sunrise Highway retail corridor and the downtown village along Rockaway Avenue. The commercial scene is heavy on retail, sit-down and quick-service restaurants, multi-tenant strip centers, and the multi-family residential that fills the western half of the village.",
        "properties": "Green Acres alone generates significant restaurant-tenant work (Class&nbsp;K throughout the food court and full-service tenants). Beyond the mall, we service Sunrise Highway big-box and strip retail, Rockaway Avenue downtown restaurants and retail, professional offices, and the multi-family residential corridors along the LIRR.",
        "nearby": "Lynbrook, Elmont, Hewlett, Malverne, Franklin Square",
    },
    {
        "slug": "rockville-centre",
        "name": "Rockville Centre",
        "zips": "11570, 11571",
        "meta_title": "Fire Extinguisher Inspection in Rockville Centre, NY — Mercy Hospital & Front Street | Y&M",
        "meta_desc": "Certified fire extinguisher service in Rockville Centre, NY. Front Street downtown, Mount Sinai South Nassau, medical offices, restaurants. Call 516-324-8078.",
        "meta_keywords": "fire extinguisher inspection Rockville Centre NY, RVC fire safety, Mercy Hospital fire extinguisher, Front Street NFPA 10",
        "subheading": "Downtown RVC, Mercy Hospital, and the Front Street commercial corridor.",
        "intro": "From Front Street&rsquo;s downtown restaurants to Mount Sinai South Nassau and the surrounding medical complex, we keep Rockville Centre&rsquo;s commercial and healthcare properties NFPA&nbsp;10 compliant.",
        "context": "Rockville Centre is a dense South Shore village with a downtown commercial spine along Front Street and Sunrise Highway. The village is anchored by Mount Sinai South Nassau (formerly South Nassau Communities / Mercy Hospital) and a surrounding medical-office cluster, plus a celebrated downtown restaurant scene that draws from across the South Shore. Multi-family residential rings the village center.",
        "properties": "RVC&rsquo;s two big drivers are healthcare and dining. The Mount Sinai South Nassau campus and surrounding medical offices generate steady CO&#8322; and ABC work; the dense restaurant scene along Front Street and North Park Avenue drives Class&nbsp;K demand. We also service the village&rsquo;s professional offices, retail, and multi-family residential.",
        "nearby": "Lynbrook, Baldwin, Hewlett, Oceanside, East Rockaway, Malverne",
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<title>{META_TITLE}</title>
<meta name="description" content="{META_DESC}" />
<meta name="keywords" content="{META_KEYWORDS}" />
<link rel="canonical" href="https://www.ymextinguishers.com/areas/{SLUG}.html" />

<meta property="og:type" content="article" />
<meta property="og:title" content="{META_TITLE}" />
<meta property="og:description" content="{META_DESC}" />
<meta property="og:url" content="https://www.ymextinguishers.com/areas/{SLUG}.html" />
<meta property="og:image" content="https://www.ymextinguishers.com/assets/og-image.jpg" />

<link rel="icon" type="image/png" href="../assets/favicon.png" />
<meta name="theme-color" content="#0a0a0b" />

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Bebas+Neue&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../styles.css" />

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://www.ymextinguishers.com/areas/{SLUG}.html#business",
  "name": "Y&M Fire Extinguisher Inspection & Services - {NAME}",
  "image": "https://www.ymextinguishers.com/assets/og-image.jpg",
  "url": "https://www.ymextinguishers.com/areas/{SLUG}.html",
  "telephone": "+1-516-324-8078",
  "email": "info@ymextinguishers.com",
  "priceRange": "$$",
  "description": "{META_DESC}",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "{NAME}",
    "addressRegion": "NY",
    "addressCountry": "US"
  },
  "areaServed": {
    "@type": "City",
    "name": "{NAME}, NY"
  }
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.ymextinguishers.com/" },
    { "@type": "ListItem", "position": 2, "name": "Service Areas", "item": "https://www.ymextinguishers.com/areas/" },
    { "@type": "ListItem", "position": 3, "name": "{NAME}", "item": "https://www.ymextinguishers.com/areas/{SLUG}.html" }
  ]
}
</script>
</head>

<body>

<div class="topbar"><div class="container topbar-inner">
  <span class="topbar-pill"><span class="dot"></span> Available now &middot; Nassau County, NY</span>
  <div class="topbar-links">
    <a href="tel:+15163248078" class="topbar-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg> 516-324-8078</a>
    <a href="mailto:info@ymextinguishers.com" class="topbar-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg> info@ymextinguishers.com</a>
  </div>
</div></div>

<header class="site-header" id="siteHeader"><div class="container header-inner">
  <a href="../index.html" class="brand"><img src="../assets/logo.png" alt="Y&M logo" class="brand-mark" /><span class="brand-text"><strong>Y&amp;M</strong><small>Fire Extinguisher Inspection &amp; Services</small></span></a>
  <nav class="nav" aria-label="Primary"><a href="../index.html#services">Services</a><a href="index.html">Service Areas</a><a href="../index.html#why">Why Y&amp;M</a><a href="../index.html#industries">Industries</a><a href="../index.html#faq">FAQ</a><a href="../index.html#contact">Contact</a></nav>
  <a href="../index.html#contact" class="btn btn-primary header-cta">Schedule Inspection</a>
  <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" id="navToggle"><span></span><span></span><span></span></button>
</div></header>

<section class="svc-hero">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Home</a><span class="sep">/</span>
      <a href="index.html">Service Areas</a><span class="sep">/</span>
      <span aria-current="page">{NAME}</span>
    </nav>
    <div style="margin-top: 30px;">
      <span class="eyebrow"><span class="eyebrow-dot"></span> Service Area &middot; Nassau County, NY</span>
      <h1>Fire extinguisher inspection in {NAME}, NY.</h1>
      <p class="lede">{SUBHEADING}</p>
      <p class="lede" style="font-size:1rem;">{INTRO}</p>
      <div class="svc-meta">
        <div><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> NFPA 10 compliant</div>
        <div><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Licensed &amp; insured</div>
        <div><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Local Nassau County inspector</div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top: 40px;">
  <div class="container svc-layout">
    <article class="svc-content">

      <h2>About {NAME}</h2>
      <p>{CONTEXT}</p>

      <h2>What we typically service in {NAME}</h2>
      <p>{PROPERTIES}</p>

      <h2>Services we provide in {NAME}</h2>
      <ul>
        <li><a href="../services/annual-inspection.html" style="color:var(--accent-2); font-weight:600;">Annual inspection &amp; tagging</a> &mdash; NFPA 10 yearly inspection with dated certification tags and a written report.</li>
        <li><a href="../services/recharge.html" style="color:var(--accent-2); font-weight:600;">Recharge &amp; refill</a> &mdash; ABC, CO&#8322;, and Class K units recharged to factory specs, often same-day.</li>
        <li><a href="../services/hydrostatic-testing.html" style="color:var(--accent-2); font-weight:600;">Hydrostatic testing</a> &mdash; 5-year and 12-year cylinder pressure tests required by NFPA 10.</li>
        <li><a href="../services/new-extinguishers.html" style="color:var(--accent-2); font-weight:600;">New extinguisher supply</a> &mdash; UL-listed equipment sized to your hazard, mounted and tagged.</li>
        <li><a href="../services/compliance-audits.html" style="color:var(--accent-2); font-weight:600;">Compliance audits</a> &mdash; pre-fire-marshal walkthrough, gap report, and on-the-spot fixes.</li>
        <li><a href="../services/multi-site-management.html" style="color:var(--accent-2); font-weight:600;">Multi-site management</a> &mdash; one vendor for portfolio-wide extinguisher service across multiple {NAME}-area properties.</li>
      </ul>

      <div class="callout">
        <strong>Worried about an upcoming fire-marshal visit in {NAME}?</strong> Send us a message or call. We&rsquo;ll do a fast walkthrough, identify exactly what needs fixing, and have you ready before the inspector arrives.
      </div>

      <h2>Areas we also serve nearby</h2>
      <p>{NEARBY}, plus all of Nassau County and Long Island.</p>

      <h2>Schedule {NAME} extinguisher service</h2>
      <p>Call <a href="tel:+15163248078" style="color:var(--accent-2); font-weight:600;">516-324-8078</a> or <a href="../index.html#contact" style="color:var(--accent-2); font-weight:600;">request a quote online</a>. Most {NAME} jobs are scheduled within the same week.</p>
    </article>

    <aside class="svc-aside">
      <div class="quick-call">
        <strong>Local to {NAME}?</strong>
        <span>Call directly for fastest scheduling.</span>
        <a href="tel:+15163248078">516-324-8078</a>
      </div>
      <div class="card">
        <h4>ZIP codes we serve</h4>
        <p style="font-size:.9rem; color:var(--text-dim); margin:0;">{ZIPS}</p>
      </div>
      <div class="card">
        <h4>Services</h4>
        <a href="../services/annual-inspection.html">Annual Inspection &amp; Tagging &rarr;</a>
        <a href="../services/recharge.html">Recharge &amp; Refill &rarr;</a>
        <a href="../services/hydrostatic-testing.html">Hydrostatic Testing &rarr;</a>
        <a href="../services/new-extinguishers.html">New Extinguisher Supply &rarr;</a>
        <a href="../services/compliance-audits.html">Compliance Audits &rarr;</a>
        <a href="../services/multi-site-management.html">Multi-Site Management &rarr;</a>
      </div>
      <div class="card">
        <h4>All Nassau County areas</h4>
        <a href="index.html" style="color:var(--accent-2); font-weight:600;">View all service areas &rarr;</a>
      </div>
    </aside>
  </div>
</section>

<section class="cta-band"><div class="container cta-inner">
  <div><h3>Serving {NAME} businesses since day one.</h3><p>Certified inspections &middot; Licensed &amp; insured &middot; Local Nassau County service.</p></div>
  <a href="tel:+15163248078" class="btn btn-primary btn-lg">Call 516-324-8078</a>
</div></section>

<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand"><img src="../assets/logo.png" alt="Y&M logo" class="brand-mark" /><p>Y&amp;M Fire Extinguisher Inspection &amp; Services. Certified, licensed, and insured. Serving Nassau County and Long Island, New York.</p></div>
    <div><h5>Services</h5><ul><li><a href="../services/annual-inspection.html">Annual inspection &amp; tagging</a></li><li><a href="../services/recharge.html">Recharge &amp; refill</a></li><li><a href="../services/hydrostatic-testing.html">Hydrostatic testing</a></li><li><a href="../services/new-extinguishers.html">New extinguisher supply</a></li><li><a href="../services/compliance-audits.html">Compliance audits</a></li><li><a href="../services/multi-site-management.html">Multi-site management</a></li></ul></div>
    <div><h5>Service areas</h5><ul><li><a href="index.html">All Nassau County areas</a></li><li>Hempstead &middot; Garden City</li><li>Mineola &middot; Hicksville</li><li>Long Beach &middot; Glen Cove</li><li>Great Neck &middot; Port Washington</li></ul></div>
    <div><h5>Contact</h5><ul><li><a href="tel:+15163248078">516-324-8078</a></li><li><a href="mailto:info@ymextinguishers.com">info@ymextinguishers.com</a></li><li>www.ymextinguishers.com</li></ul></div>
  </div>
  <div class="footer-bottom"><div class="container footer-bottom-inner"><span>&copy; <span id="year"></span> Y&amp;M Fire Extinguisher Inspection &amp; Services. All rights reserved.</span><span>Inspector: Mati E. &middot; NFPA 10 compliant</span></div></div>
</footer>

<a href="tel:+15163248078" class="float-call" aria-label="Call Y&M now"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></a>

<script>
  document.getElementById('year').textContent = new Date().getFullYear();
  const header = document.getElementById('siteHeader');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 8);
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  const toggle = document.getElementById('navToggle'); const nav = document.querySelector('.nav');
  toggle.addEventListener('click', () => { const open = nav.classList.toggle('open'); toggle.classList.toggle('open', open); toggle.setAttribute('aria-expanded', String(open)); });
</script>
</body>
</html>
'''

def render(loc):
    out = TEMPLATE
    # We have HTML content with curly braces (JSON-LD), so use placeholder replace, not .format()
    replacements = {
        "{META_TITLE}": loc["meta_title"],
        "{META_DESC}": loc["meta_desc"],
        "{META_KEYWORDS}": loc["meta_keywords"],
        "{SLUG}": loc["slug"],
        "{NAME}": loc["name"],
        "{SUBHEADING}": loc["subheading"],
        "{INTRO}": loc["intro"],
        "{CONTEXT}": loc["context"],
        "{PROPERTIES}": loc["properties"],
        "{NEARBY}": loc["nearby"],
        "{ZIPS}": loc["zips"],
    }
    # Apply replacements - longest tokens first to avoid partial matches
    for token in sorted(replacements.keys(), key=len, reverse=True):
        out = out.replace(token, replacements[token])
    return out

if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(base, "areas")
    os.makedirs(out_dir, exist_ok=True)
    for loc in LOCATIONS:
        path = os.path.join(out_dir, f"{loc['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(loc))
        print(f"Wrote {loc['slug']}.html")
    print(f"\nTotal: {len(LOCATIONS)} location pages generated.")
