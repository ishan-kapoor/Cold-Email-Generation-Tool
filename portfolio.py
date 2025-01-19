import pandas as pd
import chromadb
import uuid

def load_portfolio(filepath):
    return pd.read_csv(filepath)

def query_portfolio(df, tech_stack):
    client = chromadb.PersistentClient('vectorstore')
    collection = client.get_or_create_collection(name="Portfolio")

    if not collection.count():
        for _, row in df.iterrows():
            collection.add(
                documents=row["Techstack"],
                metadatas={"links": row["Links"]},
                ids=[str(uuid.uuid4())]
            )

    results = collection.query(query_texts=tech_stack, n_results=2)
    links = results.get('metadatas', [])
    return links
