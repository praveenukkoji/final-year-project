from predict.implementation.TestingModel import predict_disease


class PredictImageImplementation:
    def __init__(self, requests):
        self.requests = requests

    @staticmethod
    def predict_image(file_url):
        payload = []
        try:
            # Cures
            mp = {
                "Strawberry___healthy": ["No Cure."],
                "Soybean___healthy": ["No Cure."],
                "Potato___healthy": ["No Cure."],
                "Apple___healthy": ["No Cure."],
                "Tomato___healthy": ["No Cure."],
                "Raspberry___healthy": ["No Cure."],
                "Grape___healthy": ["No Cure."],
                "Pepper,_bell___healthy": ["No Cure."],
                "Peach___healthy": ["No Cure."],
                "Blueberry___healthy": ["No Cure."],
                "Cherry_(including_sour)___healthy": ["No Cure."],
                "Corn_(maize)___healthy": ["No Cure."],
                "Apple___Apple_scab": [
                    "1.Choose scab-resistant varieties of apple or crabapple trees.",
                    "2.Rake up and discard any fallen leaves or fruit on a regular basis, and never leave fallen leaves\
                     or fruit on the ground over winter. Apple scab fungus overwinters on fallen leaves and fruit.",
                    "3.Prune your apple and crabapple trees to keep their crowns open so light and air can move\
                     through. Dry leaves and fruit help to prevent initial infection.",
                    "4.Plant your apple and crabapple trees correctly, in full sun and with enough space around each\
                     tree, according to their mature size. Shade keeps water from evaporating quickly, and crowded\
                     trees are more susceptible to the disease.",
                    "5.Irrigate your trees in the early morning hours, and don’t use overhead sprays that will wet\
                     leaves and fruit. Dry leaves won’t host the fungus."
                ],
                "Apple___Black_rot": [
                    "1.Prune out dead or diseased branches.",
                    "2.Pick all dried and shriveled fruits remaining on the trees.",
                    "3.Remove infected plant material from the area.",
                    "4.All infected plant parts should be burned, buried or sent to a municipal composting site.",
                    "5.Be sure to remove the stumps of any apple trees you cut down."
                ],
                "Apple___Cedar_apple_rust": [
                    "1.Choose resistant cultivars when available.",
                    "2.Rake up and dispose of fallen leaves and other debris from under trees.",
                    "3.Remove galls from infected junipers.",
                    "4.Apply preventative, disease-fighting fungicides labeled for use on apples weekly to protect\
                     trees from spores being released by the juniper host. ",
                    "5.Rust can be controlled by spraying plants with a copper solution (0.5 to 2.0 oz/ gallon of\
                     water) at least four times."
                ],
                "Cherry_(including_sour)___Powdery_mildew": [
                    "1.Cut off all infected leaves at the very bottom of the stem.",
                    "2.Prune your plant to encourage air flow.",
                    "3.Spray your plant with milk and dish wash solution weekly."
                ],
                "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": [
                    "1.Hybrids with partial resistance to GLS are available. Ask your seed supplier for these hybrids.",
                    "2.Crop rotation and clean plowing are effective at reducing in-field inoculum buildup. A two-year\
                     crop rotation away from corn is effective if reduced tillage must be maintained for conservation\
                     purposes or a one-year rotation with clean plowing is recommended in fields that have had a problem\
                     with the disease.",
                    "3.Fungicides are available to manage gray leaf spot. These are recommended when susceptible\
                     hybrids are planted in fields with a history of gray leaf spot."
                ],
                "Corn_(maize)___Common_rust_": [
                    "1.Scout corn to detect common rust early.",
                    "2.Monitor disease development, crop growth stage and weather forecast.",
                    "3.Apply a foliar fungicide if: 3.1.Rust is spreading rapidly or likely to spread and yield\
                     may be affected. 3.2.Disease exceeds threshold established by your state extension plant\
                     pathologist 3.3.Commonly used fungicides include Aproach, Headline, Headline SC, Headline AMP,\
                     PropiMax EC, Quadris, Quilt, Quilt Xcel, Stratego, Stratego YLD and Tilt."
                ],
                "Corn_(maize)___Northern_Leaf_Blight": [
                    "1.Organic control: bio-fungisides based on tricoderma harzianum or bacillus subtilies can be\
                     applied at differnt stages to decrese the risk of infection.application of sulphur solution is\
                     also effective.",
                    "2.Chemical control: apply spray based on Picoxystrobin, mancozeb, metconazole."
                ],
                "Tomato___Bacterial_spot": [
                    "1.Disease-free seeds and transplants: Always use disease-free seeds and transplants as the first\
                     step in disease management. Scout plants for the disease daily and destroy diseased seedlings.",
                    "2.Seed treatment: Soak seeds in 10% water solution of household bleach\
                     (5.25% sodium hypochlorite) for 45 min, and rinse thoroughly. This can effectively reduce \
                     bacterial population on seed surface. Hot water treatment at 122°F for 25 min is effective in\
                     reducing bacterial population on the surface and inside the seeds, but may affect seed germination\
                     when the temperature is not properly controlled. Rinse seed in clean water immediately after\
                     treatments. The seed should be air dried prior to storing."
                ],
                "Tomato___Early_blight": [
                    "1.Remove infected plant portions. The most essential aspect of treating blight is to remove and\
                     destroy any affected area of the tomato plant. If you notice any telltale signs, prune those\
                     sections from the plant and discard them far away from your garden. As long as any sections of\
                     the plant or soil are still suffering from the fungal disease, the spores are likely to spread\
                     again.",
                    "2. Use fungicide. Utilizing a fungicide is one key way you can address your blight problem.\
                     After removing any infected leaves, you can spray the surrounding area with a copper fungicide\
                     or biofungicide to help contain the problem if it hasn’t spread too far.",
                    "3. Add mulch to the soil. Using mulch can introduce nutrients into your soil and prevent the\
                     spores from spreading further through the air. "
                ],
                "Tomato___Late_blight": [
                    "1.Plant resistant cultivars when available.",
                    "2.Remove volunteers from the garden prior to planting and space plants far enough apart to allow\
                     for plenty of air circulation.",
                    "3.Water in the early morning hours, or use soaker hoses, to give plants time to dry out during the\
                     day — avoid overhead irrigation.",
                    "4.Destroy all tomato and potato debris after harvest."
                ],
                "Tomato___Leaf_Mold": [
                    "1.Remove and destroy all affected plant parts. For plants growing under cover, increase\
                     ventilation and, if possible, the space between plants.",
                    "2.Try to avoid wetting the leaves when watering plants, especially when watering in the evening",
                    "3.Copper-based fungicides can be used to control diseases on tomatoes."
                ],
                "Tomato___Septoria_leaf_spot": [
                    "1.Use disease-free seed. There's no evidence that this fungus is carried by seeds, but err on the\
                     safe side and don't save seed from infected plants. Thoroughly processing the tomato seeds you are\
                     saving will also help rid the seeds of lingering diseases.",
                    "2.Start with a clean garden. Dispose of all affected plants. The fungus can over-winter on the\
                     debris of diseased plants. It's important to dispose of all the affected plants far away from the\
                     garden and the compost pile. Keep in mind that it may have spread to your potatoes and eggplants,\
                     too.",
                    "3.Avoid overhead watering. Water aids the spread of Septoria leaf spot. Keep it off the leaves as\
                     much as possible by watering at the base of the plant only. Of course, it's impossible to keep the\
                      rain off your plants, but every little bit helps.",
                    "4.Provide room for air circulation. Leave some space between your tomato plants so there is good\
                     airflow. Stake them so that they are not touching the ground and not all bunched together. Good\
                     air circulation is especially important during damp and rainy periods.",
                    "5.Mulch below the plants. A layer of mulch will help prevent spores on the ground from splashing\
                     up onto the lower leaves.",
                    "6.Plant next year's tomatoes in a different section of your garden. In small gardens, it's not\
                     always practical to rotate your crops, so good clean up and sanitation become even more important."
                ],
                "Tomato___Spider_mites Two-spotted_spider_mite": [
                    "1.Avoid weedy fields and do not plant eggplant adjacent to legume forage crops.",
                    "2.Avoid early season, broad-spectrum insecticide applications for other pests.",
                    "3.Do not over-fertilize.",
                    "4.Overhead irrigation or prolonged periods of rain can help reduce populations.",
                    "5.use selective products whenever possible spirotetramat\
                     (Movento): Group 23, mainly affects immature stages spiromesifen\
                     (Oberon 2SC): Group 23, mainly affects immature stages",
                ],
                "Tomato___Target_Spot": [
                    "1.Before planting: Do not plant new crops next to older ones that have the disease. Plant as far\
                     as possible from papaya, especially if leaves have small angular spots (Photo 5). Check all\
                     seedlings in the nursery, and throw away any with leaf spots.",
                    "2.During growth: Remove a few branches from the lower part of the plants to allow better airflow\
                     at the base. Remove and burn the lower leaves as soon as the disease is seen, especially after the\
                     lower fruit trusses have been picked. Keep plots free from weeds, as some may be hosts of the\
                     fungus. Do not use overhead irrigation; otherwise, it will create conditions for spore production\
                     and infection.",
                    "3.After harvest: Collect and burn as much of the crop as possible when the harvest is complete.\
                     Practise crop rotation, leaving 3 years before replanting tomato on the same land."
                ],
                "Tomato___Tomato_mosaic_virus": [
                    "1.Fungicides will NOT treat this viral disease.",
                    "2.Plant resistant varieties when available or purchase transplants from a reputable source.",
                    "3.Do NOT save seeds from infected crops.",
                    "4.Spot treat with least-toxic, natural pest control products, such as Safer Soap, Bon-Neem, and\
                     diatomaceous earth, to reduce the number of disease-carrying insects.",
                    "5.Harvest-Guard® row cover will help keep insect pests off vulnerable crops/ transplants and\
                     should be installed until bloom.",
                    "6.Remove all perennial weeds, using least-toxic herbicides, within 100 yards of your garden plot.",
                    "7.The virus can be spread through human activity, tools, and equipment. Frequently wash your hands\
                     and disinfect garden tools, stakes, ties, pots, greenhouse benches, etc. (one part bleach to 4\
                     parts water) to reduce the risk of contamination.",
                    "8.Avoid working in the garden during damp conditions (viruses are easily spread when plants are\
                     wet).",
                    "9.Avoid using tobacco around susceptible plants. Cigarettes and other tobacco products may be\
                     infected and can spread the virus.",
                    "10.Remove and destroy all infected plants (see Fall Garden Cleanup). Do NOT compost."
                ],
                "Tomato___Tomato_Yellow_Leaf_Curl_Virus": [
                    "1.Imidacloprid should be sprayed on the entire plant and below the leaves; eggs and flies are\
                     often found below the leaves. Spray every 14-21 days and rotate on a monthly basis with Abamectin\
                     so that the whiteflies do not build-up resistance to chemicals.",
                    "2.Chemicals are most effective when used early in the morning and late in the evening. This is\
                     because insects are most active at these times of the day.",
                    "3.Plants that show signs of the virus after 3-4 weeks of transplanting should be bagged (to\
                     prevent the whiteflies leaving), uprooted and burned to reduce spread of the virus.",
                    "4.Plants should be watered and fertilized adequately to reduce stress and to build plant health."
                ],
                "Grape___Black_rot": [
                    "Cultural Practices for control of Grape black Rot:",
                    "1.Sanitation is extremely important. Destroy mummies, remove diseased tendrils from the wires, and\
                     select fruiting canes without lesions.",
                    "It is very important not to leave mummies attached to the vine. Research has shown that mummies on\
                     the ground release most or all of their ascospores before the end of bloom. Mummies left up in the\
                     trellis can produce ascospores and conidia throughout the growing season, thus making control of\
                     this disease much more difficult.",
                    "If only a few leaf lesions appear in the spring, remove these infected leaves.",
                    "2.Plant grapes in sunny open areas that allow good air movement. If your vines are planted under\
                     trees in the shade where they do not get all day sunlight, black rot will be much more difficult\
                     to control. ",
                    "3.Shaded areas keep the leaves and fruits from drying and provide excellent conditions for black rot\
                     infection and disease development."
                ],
                "Grape___Esca_(Black_Measles)": [
                    "Till date there is no effective method to control this disease. Remove the infected berries,\
                     leaves and trunk and destroy them. Protect the prune wounds to minimize fungal infection using\
                     wound sealant (5% boric acid in acrylic paint) or essential oil or suitable fungicides."
                ],
                "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": [
                    "Fungicides sprayed for other diseases in the season may help to reduce this disease."
                ],
                "Orange___Haunglongbing_(Citrus_greening)": [
                    "1.Spray trees with a pyrethroid (e.g., lambda-cyhalothrin) insecticide to kill the adults and\
                     nymphs. Malathion can also be used.",
                    "2.Spray the ground around trees with a systemic product (e.g., imidacloprid) so that it is taken\
                     up by the roots to kill nymphs in the folds of leaves in the canopy. Note, do not use imidacloprid\
                     when trees are flowering as it is toxic to bees.",
                    "3.As an alternative to synthetic products, use 'soft' insecticides, e.g., horticultural spray oil,\
                     neem or insecticidal soap. These treatments give protection for 9-12 months."
                ],
                "Peach___Bacterial_spot": [
                    "This disease is difficult to control, and chemical sprays are not practical for the home gardener.\
                     Varieties are available that are moderately resistant but not immune. These varieties are\
                     ‘Ambergem’, ‘Belle of Georgia’, ‘Cardinal’, ‘Cherryred’, ‘Dixired’, ‘Candor,’ ‘Challenger’,\
                     ‘Carolina Gold’, ‘Norman,’ ‘Loring,’ ‘Bisco’, ‘Southhaven’, and ‘Red Haven’ in a yellow peach, and\
                     ‘Southern Pearl’, ‘White County’, and ‘White River’ in a white peach. Bacterial spot is usually\
                     more severe on poorly nourished trees or where nematodes are a problem, so proper cultural care\
                     is important."
                ],
                "Pepper,_bell___Bacterial_spot": [
                    "1.The most effective management strategy is the use of pathogen-free certified seeds and\
                     disease-free transplants to prevent the introduction of the pathogen into greenhouses and field\
                     production areas. Inspect plants very carefully and reject infected transplants- including your\
                     own!",
                    "2.In the greenhouse, discard trays adjacent to outbreak location to minimize disease spread.",
                    "3.Treat seeds with dilute bleach, hydrochloric acid, or hot water to reduce the potential for\
                     seedling infection. These treatments may also reduce seed germination. Perform a test treatment on\
                     approximately 50 to 100 seeds and check for the effect on germination before treating an entire\
                     seed lot.",
                    "4.In transplant production greenhouses, minimize overwatering and handling of seedlings when they\
                     are wet.",
                    "5.Trays, benches, tools, and greenhouse structures should be washed and sanitized between\
                     seedlings crops.",
                    "6.Crop rotation should be used to avoid pathogen carryover on volunteers and crop residue.\
                     Avoid fields that have been planted with peppers or tomatoes within one year, especially if they\
                     had bacterial spot previously.",
                    "7.Eliminate solanaceous weeds in and around tomato and pepper production areas.",
                    "8.Keep cull piles away from field operations.",
                    "9.Do not spray, tie, harvest, or handle wet plants as that can spread the disease."
                ],
                "Potato___Early_blight": [
                    "1.Prune or stake plants to improve air circulation and reduce fungal problems.",
                    "2.Make sure to disinfect your pruning shears (one part bleach to 4 parts water) after each cut.",
                    "3.Keep the soil under plants clean and free of garden debris. Add a layer of organic compost to\
                     prevent the spores from splashing back up onto vegetation.",
                    "4.Drip irrigation and soaker hoses can be used to help keep the foliage dry.",
                    "5.For best control, apply copper-based fungicides early, two weeks before disease normally appears\
                     or when weather forecasts predict a long period of wet weather. Alternatively, begin treatment\
                     when disease first appears, and repeat every 7-10 days for as long as needed.",
                    "6.Containing copper and pyrethrins, Bonide® Garden Dust is a safe, one-step control for many\
                     insect attacks and fungal problems. For best results, cover both the tops and undersides of leaves\
                     with a thin uniform film or dust. Depending on foliage density, 10 oz will cover 625 sq ft.\
                     Repeat applications every 7-10 days, as needed."
                ],
                "Potato___Late_blight": [
                    "1.Destroy all cull and volunteer potatoes.",
                    "2.Plant late blight-free seed tubers.",
                    "3.Do not mix seed lots because cutting can transmit late blight.",
                    "4.Use a seed piece fungicide treatment labeled for control of late blight.",
                    "5.Avoid planting problem areas that may remain wet for extended periods or may be difficult to\
                     spray.",
                    "6.Avoid excessive and/or nighttime irrigation.",
                    "7.Eliminate sources of inoculum such as hairy nightshade weed species and volunteer potatoes.",
                    "8.Scout fields regularly, especially in low, wet areas, along tree lines, at the center of the\
                     pivot and other areas that remain wet for longer periods where late blight first may occur.",
                    "9.Use foliar fungicides on a regular and continuing schedule. Once late blight is present, only\
                     foliar fungicide applications can manage late blight in the field.",
                    "10.Keep up to date on late blight forecasts.",
                    "11.Quickly destroy hot spots of late blight.",
                    "12.Kill vines completely two to three weeks before harvest. Consider adding a fungicide when\
                     vine killing if there is late blight pressure.",
                    "13.Applying phosphorous acid to potatoes after harvest and before piling can prevent infection\
                     and the spread of late blight in storage.",
                    "14.Monitor home garden and market tomatoes near you for late blight. Late blight can move from\
                     these local sources to potato fields."
                ],
                "Squash___Powdery_mildew": [
                    "1.Provide good air circulation by spacing squash plants several feet apart.",
                    "2.Don’t touch infected leaves and then touch healthy leaves.",
                    "3.Always plant squash in the full sun. Shady conditions are more humid and that encourages spore\
                     germination.",
                    "4.Cut off any leaves that show early signs of infection ASAP. Toss them in the garbage or burn\
                     pile. Keep them out of the compost pile.",
                    "5.Do not apply nitrogen fertilizer in the middle of the growing season. Doing so causes a flush of\
                     new growth which is more prone to the disease.",
                    "6.Remove and destroy all infected plants at the end of the growing season to get rid of as many\
                     spores as possible. Do not compost them; throw them in the garbage, or bury or burn them."
                ],
                "Strawberry___Leaf_scorch": [
                    "1.Start with certified, disease-free plants purchased from a reputable nursery.",
                    "2.These cultural practices help reduce infections.",
                    "3.Plant in full sunlight in well-drained soil with good air circulation.",
                    "4.Prevent weed growth by cultural or chemical methods.",
                    "5.Take care in spacing runner plants in matted-row culture. Do not allow an over-population of\
                     plants.",
                    "6.Always remove the old infected leaves from runner plants before setting.",
                    "7.Apply nitrogen fertilizers only at renovation time. Applications of nitrogen in the spring\
                     produce an overabundance of young leaf tissue susceptible to leaf-disease fungi."
                ]
            }

            # jupyter notebook code start

            path_to_file = 'predict/implementation/media/' + file_url
            print(path_to_file)
            ans = predict_disease(path_to_file)
            print(ans)
            payload.append({"Plant Name": ans.split("___")[0], "Plant Disease": ans.split("___")[1],
                            "Cure Steps": mp[ans]})

            # jupyter notebook code end
        except Exception as e:
            print(e)
            raise e
        return payload