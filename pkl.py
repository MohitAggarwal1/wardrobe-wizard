import pickle

# Sample fashion recommendations dictionary for demonstration
fashion_recommendations = {
    ('Male', 'Slim', 'Fair', 'Casual'): [
        {
            'name': 'BULLMER Trendy Clothing Set',
            'image': 'https://m.media-amazon.com/images/I/61JxTwwj-5L._SY741_.jpg',
            'link': 'https://www.amazon.in/BULLMER-Trendy-Clothing-Co-ords-XXXX-Large/dp/B0CT8YM8WK?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=AB57CX8LB83EF'
        },
        {
            'name': 'BULLMER Trendy Clothing Set',
            'image': 'https://m.media-amazon.com/images/I/61JxTwwj-5L._SY741_.jpg',
            'link': 'https://www.amazon.in/BULLMER-Trendy-Clothing-Co-ords-XXXX-Large/dp/B0CT8YM8WK?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=AB57CX8LB83EF'
        },
        {
            'name': 'BULLMER Trendy Clothing Set',
            'image': 'https://m.media-amazon.com/images/I/61JxTwwj-5L._SY741_.jpg',
            'link': 'https://www.amazon.in/BULLMER-Trendy-Clothing-Co-ords-XXXX-Large/dp/B0CT8YM8WK?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=AB57CX8LB83EF'
        },
        {
            'name': 'CLAFOUTIS Men Ribbed T-Shirt & Shorts',
            'image': 'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcTy8Uf2U_r30MmFgzbtk2hkkM-IR1F5x8iwjcspbHpXt2viPJn768nKcUw8Tc3YjDAiEUPjzMMCpxkRvjQ0qZSNaHBNvvr1XQrKiJNcWUNg&usqp=CAE',
            'link': 'https://www.google.com/shopping/product/14881720635698900100?sca_esv=91c658cd3c6ca43c&rlz=1C1RXQR_enIN1116IN1116&sxsrf=ADLYWIJ259hcUn_DeEnfJnBiIeHpGKS_jA:1730279652501&q=male+casual+outfits&fbs=AEQNm0CvspUPonaF8UH5s_LBD3JPX4RSeMPt9v8oIaeGMh2T2PRrsfVPlQRxSTpQ4UUI6wfsFlEVaMALnJjEZtYpSTLmo53r2zppOiIGuIbqiAjNkwbNaijPbCFlH3Cy3DXsEI7zMW6ofoiQ4sgXJTK-wBJP5rXDgIm0ZxzY8Uu4bv5bqHnOH2mdS4OXWmns-rV0M2hOXLXXeFWHyv-E6HJzCSEkPFws3Q&ictx=111&biw=1350&bih=625&dpr=1&prds=eto:3373009415023619929_0,pid:8133352035216811489&sa=X&ved=0ahUKEwj-r-fT4rWJAxXOTGwGHXTzE0EQ8gIIogsoAA'
        }
    ],
    ('Female', 'Curvy', 'Brown', 'Party'): [
        {
            'name': 'Off-shoulder dress with heels',
            'image': 'https://example.com/image2.jpg',
            'link': 'https://myntra.com/outfit2'
        },
        {
            'name': 'Off-shoulder dress with heels',
            'image': 'https://example.com/image2.jpg',
            'link': 'https://myntra.com/outfit2'
        }
    ]
}


# Save this data as a pickle file
with open('fashion_model.pkl', 'wb') as file:
    pickle.dump(fashion_recommendations, file)

print("fashion_model.pkl has been created.")
