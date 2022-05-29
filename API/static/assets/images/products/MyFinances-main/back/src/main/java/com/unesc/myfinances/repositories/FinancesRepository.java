package com.unesc.myfinances.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.unesc.myfinances.entities.Finances;

@Repository
public interface FinancesRepository extends JpaRepository<Finances, Long>{

}
